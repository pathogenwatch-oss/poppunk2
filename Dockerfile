FROM continuumio/miniconda3:24.3.0-0 as base

COPY environment.yml /

ENV PYTHONDONTWRITEBYTECODE=true

RUN conda env create -f environment.yml \
    && conda clean -a \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete

FROM base

ARG LIBRARY=vibriowatch

LABEL authors="Anthony Underwood & Corin Yeats" \
      description="Docker image PopPUNK2"

COPY ${LIBRARY}_db/ /${LIBRARY}_db/
# COPY gpsc_clusters.csv /
COPY sample.txt /
COPY result2json.py /
COPY versions.json /
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENV LIB=${LIBRARY}

ENTRYPOINT /entrypoint.sh ${LIB}
