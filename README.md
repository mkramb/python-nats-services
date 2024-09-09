# Python NATS Microservices

## Prerequisite

Install poetry & dependencies:

```
curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.in-project true
poetry install
```

Setting up local cluster:

```
sh .tools/cluster-delete.sh
sh ./tools/cluster-create.sh
```

## Usage

Starting services for local development:

```
task start-consumer
task start-publisher
```

Running the full k8s stack:

```
tilt up

# to stop current pods
# and clear any defined CRDs
tilt down
```
