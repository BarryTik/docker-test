FROM python:3.9

RUN apt-get update && apt-get install -y \
    wget

WORKDIR /home
RUN cd /home && \
    curl -L https://api.github.com/repos/tikal004/dockerfail/tarball | tar xz --strip=1
ENTRYPOINT [ "/home/app.py" ]