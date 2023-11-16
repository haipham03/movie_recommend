FROM ubuntu:20.04

WORKDIR /recommend

RUN --mount=type=cache,target=/root/.cache \
    apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates \
    libusb-1.0-0 \
    libjpeg-dev \
    libpng-dev \
    libgl1 \
    usbutils \
    libglib2.0-0 \
    git \
    wget \
    vim \
    tmux \
    gcc \
    software-properties-common

RUN --mount=type=cache,target=/root/.cache \
    apt-get update -y \
    && apt-get install -y python3-pip \
    && pip3 install -U pip \
    && pip3 install pyem empy pyyaml

COPY . /recommend/

RUN --mount=type=cache,target=/root/.cache \
    pip3 install gdown

RUN --mount=type=cache,target=/root/.cache \
    cd /recommend && \
    pip3 install -r requirements.txt