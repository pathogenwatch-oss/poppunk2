FROM continuumio/miniconda3:4.9.2
LABEL authors="Anthony Underwood" \
      description="Docker image PopPUNK2"

COPY environment.yml /
RUN conda env create -f environment.yml && conda clean -a

COPY ref/ /ref/
COPY gpsc_clusters.csv /
COPY sample.txt /
COPY result2json.py /

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
