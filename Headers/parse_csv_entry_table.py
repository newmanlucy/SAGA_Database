# python 3.5

# uses file list instead of os walk

import os
import csv

file_dir = "./file_list.txt"
list_header = {}

with open(file_dir, "r") as f_dir:
    for line in f_dir:
        with open(line.strip()) as f_curr:
            csv_reader = csv.reader(csv_file)
            curr_headers = next(csv_reader)
            for col in curr_headers:
                if col in list_headers:
                    list_header[col].append(
            
