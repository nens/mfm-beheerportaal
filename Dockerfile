FROM ubuntu:bionic

# Get rid of debconf messages like "unable to initialize frontend: Dialog".
# https://github.com/docker/docker/issues/4032#issuecomment-192327844
ARG DEBIAN_FRONTEND=noninteractive

# Note: The official Debian and Ubuntu images automatically run apt-get clean,
# so explicit invocation is not required. See RUN apt-get in "Best practices
# for writing Dockerfiles". https://docs.docker.com/engine/userguide/↵
# eng-image/dockerfile_best-practices/
#
# Installing psycopg2 via pip requires libpq-dev. The latter is also a
# dependency of libgdal-dev, but explicit is better than implicit.
RUN apt-get update && apt-get install -y \
    git \
    libpq-dev \
    memcached \
    python3-dev \
    python3-pip \
    locales \
    tzdata \
&& apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8

# Set timezone to the same as our servers, Europe/Amsterdam
# Needs tzdata installed
ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Create a nens user and group, with IDs matching those of the developer.
# The default values can be overridden at build-time via:
#
# docker-compose build --build-arg uid=`id -u` --build-arg gid=`id -g` web
#
# The -l option is to fix a problem with large user IDs (e.g. 1235227245).
# https://forums.docker.com/t/run-adduser-seems-to-hang-with-large-uid/27371/3
# https://github.com/moby/moby/issues/5419
ARG uid=1000
ARG gid=1000
RUN groupadd -g $gid nens && useradd -lm -u $uid -g $gid nens

RUN pip3 install --upgrade setuptools pip pipenv

VOLUME /code
WORKDIR /code
USER nens
