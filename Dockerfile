FROM nvcr.io/nvidia/pytorch:21.11-py3

WORKDIR /home
RUN cd /home && \
    curl -L https://api.github.com/repos/tikal004/docker-test/tarball/pytorch | tar xz --strip=1
RUN chmod +x /home/app.py    
ENTRYPOINT [ "/home/app.py" ]