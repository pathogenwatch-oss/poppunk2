import csv
import json
import sys
import os

result_file = "result/result_external_clusters.csv"
# read in lineage report
if os.path.exists(result_file):
    with open(result_file) as result:
        reader = csv.DictReader(result)
        try:
            result_info = next(reader)
            # convert to JSON
            if result_info['GPSC'] == "NA":
                print(json.dumps({'strain' : "Not assigned"}))
            else:
                print(json.dumps({'strain' : result_info['GPSC']}))
        except StopIteration:
            print(json.dumps({'strain' : "Not assigned"}))

else:
    print("Result file not found")
    sys.exit(1)
