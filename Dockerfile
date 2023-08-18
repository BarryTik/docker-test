FROM python:3.9
WORKDIR /home
RUN cd /home && \
    git clone git@github.umn.edu:tikal004/dockerfail.git
ENTRYPOINT [ "/home/dockerfail/app.py" ]