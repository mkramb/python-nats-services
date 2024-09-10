# Python NATS Microservices

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
