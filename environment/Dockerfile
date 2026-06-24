# hash:sha256:62b1b398c26eb1cce4bff47627650828dd742b34fa1d9aadb8f6f091e482e20b
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/miniconda3:25.3.0-3-python3.12.10-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG GIT_ASKPASS
COPY git-ask-pass /

RUN pip3 install -U --no-cache-dir \
    growthcurves==0.9.0 \
    kaleido==0.2.1 \
    numpy==2.3.5 \
    openpyxl==3.1.5 \
    pandas==2.3.3 \
    plotly==6.3.1 \
    pyod==2.0.7 \
    scipy==1.16.3 \
    st-selectable-grid==1.0.0 \
    streamlit==1.52.0 \
    streamlit-aggrid==1.2.1 \
    streamlit-sortables==0.3.1 \
    xlrd==2.0.2
