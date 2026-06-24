# hash:sha256:db618a8e33088c187ce3a0e2ecd7cdcd84c0e5a31c2a510662e4d393f4f0f5c8
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/py-r:python3.10.12-R4.2.3-IRkernel-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG GIT_ASKPASS
COPY git-ask-pass /

RUN pip3 install -U --no-cache-dir \
    growthcurves \
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
