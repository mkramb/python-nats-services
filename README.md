# Python NATS Microservices

## Prerequisite

```
brew install kind
brew install tilt-dev/tap/tilt
brew install tilt-dev/tap/ctlptl
```

Setting up local cluster:

```
sh .tools/cluster-delete.sh
sh ./tools/cluster-create.sh
```