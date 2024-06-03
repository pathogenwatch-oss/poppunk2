import argparse
import csv
import json
import os
import sys


def result2json(result_file, metadata_file: str, versions_file: str, key: str) -> None:
    """
    Reads metadata and versions files, then reads in a lineage report from a CSV file.
    If the result file exists, it reads the first row and converts it to JSON.
    If the key in the result file is "NA", it sets the strain to "Not assigned".
    Otherwise, it uses the strain from the result file.

    Parameters:
    - result_file (str): The path to the result file.
    - metadata_file (str): The path to the metadata file.
    - versions_file (str): The path to the versions file.
    - key (str): The assigned code tag, e.g. "GPSC".

    Returns:
    None. The function prints the JSON-formatted metadata and strain information.
    """
    # Read metadata file
    if os.path.exists(metadata_file):
        with open(metadata_file) as f:
            metadata = json.load(f)
    else:
        exit("Metadata file not found")

    # Read versions file
    if os.path.exists(versions_file):
        with open(versions_file) as versions_f:
            versions = json.load(versions_f)
    else:
        exit("Versions file not found")

    metadata["versions"] = {**metadata["versions"], **versions}

    # read in lineage report
    if os.path.exists(result_file):
        with open(result_file) as result:
            reader = csv.DictReader(result)
            try:
                result_info = next(reader)
                # convert to JSON
                if result_info[key] == "NA":
                    print(json.dumps(metadata | {"strain": "Not assigned"}))
                else:
                    print(json.dumps(metadata | {"strain": result_info[key]}))
            except StopIteration:
                print(json.dumps(metadata | {"strain": "Not assigned"}))

    else:
        print("Result file not found")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("result_file", help="Result file path")
    parser.add_argument("metadata_file", help="Metadata file path")
    parser.add_argument(
        "-v",
        "--versions",
        dest="versions_file",
        help="Path to the code versions data file",
        default="versions.json",
    )
    parser.add_argument(
        "-k", "--key", help='Assigned code tag, e.g. "GPSC"', default="Cluster"
    )
    result2json(**vars(parser.parse_args()))
