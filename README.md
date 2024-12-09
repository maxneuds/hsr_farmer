# Setup

Get your `uid` and `gid` and also the `docker` group id by running `id` and then make sure to adjust the parameters at the top of the Dockerfile accordingly:

```
ENV username worker
ENV GID 1000
ENV UID 1000
ENV DOCKER_GID 965
```

# QT (xcb)

On host run:

```
xhost +si:localuser:$(whoami)
```

Maybe on container:
```
sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
```
