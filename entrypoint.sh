#!/bin/bash
set -eu -o pipefail

LIBRARY=${1}
LIBRARY_DIR=${LIBRARY}_db
METADATA=${LIBRARY_DIR}/metadata.json

OPTS=""
RESULT_DIR="result"
RESULT="${RESULT_DIR}/result_clusters.csv"
KEY="Cluster"

if [ -f ${LIBRARY}_db/${LIBRARY}_clusters.csv ]; then
    OPTS="--external-clustering ${LIBRARY_DIR}/${LIBRARY}_clusters.csv"
    RESULT="${RESULT_DIR}/result_external_clusters.csv"
    KEY=${LIBRARY^^}
fi

cat - > sequence.fas

conda run -n poppunk poppunk_assign --db /${LIBRARY_DIR} --query sample.txt ${OPTS} --output result > /dev/null 2>&1

python result2json.py ${RESULT} ${METADATA} ${KEY}