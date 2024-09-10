# Python Microservices (with NATS broker)

- the foundation is FastAPI which is a modern & fast (high-performance) framework
- for handling events we utilize FastStream (integrates with FastAPI) for effortless event stream integration
- lastly, the monorepo setup is configured so every service lists it's own dependencies

## Prerequisite

Install & setup [direnv](https://direnv.net/):

```
brew install direnv
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
```

Install latest version of [devbox](https://www.jetify.com/devbox/):

```
curl -fsSL https://get.jetify.com/devbox | bash
```

Initialize setup scripts:

```
task setup
```

## Usage

Running the full k8s stack:

```
tilt up

# to stop current pods
# and clear any defined CRDs
tilt down
```

Then we can execute:

```
curl -i http://localhost:3001/emit
```

- which should trigger a message from the publisher service
- that is then processed by the consumer service (check the logs)
