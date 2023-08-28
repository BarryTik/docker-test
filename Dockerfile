FROM python:3.9

WORKDIR /home
RUN cd /home && \
    curl -L https://api.github.com/repos/tikal004/dockerfail/tarball | tar xz --strip=1
RUN chmod +x /home/app.py    
ENTRYPOINT [ "/home/app.py" ]