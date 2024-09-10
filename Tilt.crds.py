load("ext://helm_resource", "helm_resource", "helm_repo")

NACK_VERSION = "v0.14.0"


def get_crd_name(c):
    return c["metadata"]["name"]


def get_crd_kind(c):
    return c["kind"]


def init_nats_crds():
    # install the JetStream CRDs, using local copy to avoid download flake
    bundle = local(
        "cat ./.k8s/nack-manifests/" + NACK_VERSION + ".crds.yml", quiet=True
    )
    k8s_yaml(bundle)

    # install NATS Controllers
    helm_repo(
        "nats-helm-repo", "https://nats-io.github.io/k8s/helm/charts/", labels=["infra"]
    )
    helm_resource(
        "nats-nack",
        "nats-helm-repo/nack",
        flags=["--set=jetstream.nats.url=nats://nats:4222"],
        resource_deps=["nats"],
        labels=["infra"],
    )

    jetstream_crds = [
        r
        for r in decode_yaml_stream(bundle)
        if (get_crd_kind(r) == "CustomResourceDefinition")
    ]

    if len(jetstream_crds):
        print(
            "CRDs: Importing NATS JetStream CRDs:",
            [("%s" % get_crd_name(c)) for c in jetstream_crds],
        )

        # deploy Nack CRDs as a separate resource,
        # after the operator is available
        k8s_resource(
            new_name="nats-nack-crds",
            objects=[("%s" % get_crd_name(c)) for c in jetstream_crds],
            resource_deps=["nats-nack"],
            labels=["infra"],
        )

    # loading custom config for Streams & Consumers
    custom_config = read_file(".k8s/jetstream.yml")
    custom_config_crds = [
        r
        for r in decode_yaml_stream(custom_config)
        if (get_crd_kind(r) == "Stream" or get_crd_kind(r) == "Consumer")
    ]

    print(
        "CRDs: Configuring Streams & Consumer:",
        [("%s:%s" % (get_crd_name(c), get_crd_kind(c))) for c in custom_config_crds],
    )

    k8s_yaml(".k8s/jetstream.yml")
    k8s_resource(
        new_name="nats-config",
        objects=[
            ("%s:%s" % (get_crd_name(c), get_crd_kind(c))) for c in custom_config_crds
        ],
        resource_deps=["nats-nack-crds"],
        labels=["infra"],
    )
