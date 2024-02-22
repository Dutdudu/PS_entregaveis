FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

RUN apt update && apt install tmux -y && apt install htop -y

RUN cd root && mkdir dir1 && cd dir1 && mkdir dir2 && mkdir dir3

RUN echo "set -g mouse on" >> /root/.tmux.conf

WORKDIR /root/dir1