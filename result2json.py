import csv
import json
import sys
import os

result_file = "result/result_external_clusters.csv"
# read in lineage report
if os.path.exists(result_file):
    with open(result_file) as result:
        reader = csv.DictReader(result)
        result_info = next(reader)
    # convert to JSON
    print(json.dumps({'strain' : result_info['GPSC']}))
else:
    print("Result file not found")
    sys.exit(1)
