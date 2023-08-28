FROM python:3.9

RUN apt-get update && apt-get install -y \
    wget

WORKDIR /home
RUN cd /home && \
    wget https://api.github.umn.edu/repos/tikal004/dockerfail/archive/refs/tags/v1.0.tar.gz -O archive.tgz && \
    tar -xz v1.0.tar.gz
ENTRYPOINT [ "/home/dockerfail/app.py" ]