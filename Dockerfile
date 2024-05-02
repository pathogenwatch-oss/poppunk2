FROM continuumio/miniconda3:23.10.0-1 as base

COPY environment.yml /

RUN conda env create -f environment.yml && conda clean -a

FROM base

ARG LIBRARY=vibriowatch

LABEL authors="Anthony Underwood & Corin Yeats" \
      description="Docker image PopPUNK2"

COPY ${LIBRARY}_db/ /${LIBRARY}_db/
# COPY gpsc_clusters.csv /
COPY sample.txt /
COPY result2json.py /

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENV LIB=${LIBRARY}

ENTRYPOINT /entrypoint.sh ${LIB}
