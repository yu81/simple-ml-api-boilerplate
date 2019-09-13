FROM debian:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install \
    numpy \
    pandas \
    scikit-learn \
    keras \
    tensorflow \
    scipy \
    mypy \
    joblib \
    responder && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
