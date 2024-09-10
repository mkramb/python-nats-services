load("Tiltfile.crds", "init_nats_crds")
load("Tiltfile.services", "define_service", "build_service")

update_settings(max_parallel_updates=5)
docker_prune_settings(
  disable=False,
  num_builds=3,
  keep_recent=2
)

k8s_yaml(".k8s/nats.yaml")
k8s_resource("nats", port_forwards=["4222:4222"])

init_nats_crds()

build_service("consumer")
build_service("publisher")

define_service("consumer", ["3000:3000"], ["nats","nats-nack"])
define_service("publisher", ["3001:3000"], ["nats","nats-nack"])
