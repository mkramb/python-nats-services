docker_prune_settings(
  disable=False,
  num_builds=3,
  keep_recent=2
)

k8s_yaml(".k8s/nats.yaml")
k8s_resource("nats", port_forwards=["4222:4222"])
