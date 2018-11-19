import re
import sys

def sort_uuids(file_name):
    try:
        in_file  = open("sample.txt", "r")
        out_file = open("results.txt", "w")
    except Exception as e:
        print("Failed to open the file \"sample.txt\": {}".format(e), file=sys.stderr)
        raise

    lines = in_file.readlines()
    lines.sort(key=lambda x: x.split("-")[1] if len(x.split("-")) > 1 else x.split("-")[0])
    try:
        for line in lines:
            out_file.write(line)
    except Exception as e:
        print(e, file=sys.stderr)

sort_uuids("sample.txt")