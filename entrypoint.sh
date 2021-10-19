#!/bin/bash
set -eu -o pipefail

cat - > sequence.fas

conda run -n poppunk poppunk_assign --db /ref --query sample.txt --external-clustering gpsc_clusters.csv --output result > /dev/null 2> /dev/null

python result2json.py