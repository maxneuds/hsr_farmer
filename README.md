# Setup

Get your `uid` and `gid` and also the `docker` group id by running `id` and then make sure to adjust the parameters at the top of the Dockerfile accordingly:

```
ENV username worker
ENV GID 1000
ENV UID 1000
ENV DOCKER_GID 965
```


