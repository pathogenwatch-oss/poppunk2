import csv
import json
import os
import sys

# "result/result_external_clusters.csv"
result_file = sys.argv[1]
metadata_file = sys.argv[2]
key = 'Cluster' if len(sys.argv) == 3 else sys.argv[3]

# Read metadata file
if os.path.exists(metadata_file):
    with open(metadata_file) as metadata:
        metadata = json.load(metadata)
else:
    exit("Metadata file not found")

# read in lineage report
if os.path.exists(result_file):
    with open(result_file) as result:
        reader = csv.DictReader(result)
        try:
            result_info = next(reader)
            # convert to JSON
            if result_info[key] == "NA":
                print(json.dumps(metadata | {'strain': "Not assigned"}))
            else:
                print(json.dumps(metadata | {'strain': result_info[key]}))
        except StopIteration:
            print(json.dumps(metadata | {'strain': "Not assigned"}))

else:
    print("Result file not found")
    sys.exit(1)
