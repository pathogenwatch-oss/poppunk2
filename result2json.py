import csv
import json
import os
import sys

# "result/result_external_clusters.csv"
result_file = sys.argv[1]
key = 'Cluster' if len(sys.argv) == 2 else sys.argv[2]
# read in lineage report
if os.path.exists(result_file):
    with open(result_file) as result:
        reader = csv.DictReader(result)
        try:
            result_info = next(reader)
            # convert to JSON
            if result_info[key] == "NA":
                print(json.dumps({'strain': "Not assigned"}))
            else:
                print(json.dumps({'strain': result_info[key]}))
        except StopIteration:
            print(json.dumps({'strain': "Not assigned"}))

else:
    print("Result file not found")
    sys.exit(1)
