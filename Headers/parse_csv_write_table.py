# python 3.5

import os
import csv

rootdir = ""
file_dir = "file_list.txt"

if os.path.exists(rootdir + "full_table.txt"):
    print("Error: File already exists")
else:
   open(rootdir + "full_table.txt", "w")

## get a dictionary of all the headers connected to a list
## of the files that contain those headers

data_read = []
file_data = {}
list_headers = []

with open(file_dir, "r") as f_dir:
    for line in f_dir:
        path = line.strip()
        with open(path) as csv_file, open(path) as csv_file2:
            csv_dict_reader = csv.DictReader(csv_file)
            csv_reader = csv.reader(csv_file2)
            for row in csv_dict_reader:
                print(row)
                data_read.update(row)
            header = next(csv_reader)
            print(header)

print(data_read)
