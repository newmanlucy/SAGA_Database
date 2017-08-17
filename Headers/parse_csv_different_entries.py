import os
import csv

rootdir = "/home/user/Desktop/sgsg/Testing/CSV/NCHS001.s0403_040808 v"


## get a dictionary of all the headers connected to a list
## of the files that contain those headers
dict_1 = {}

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        full_path = os.path.join(subdir, file)
        print(full_path)
        filename, file_extension = os.path.splitext(file)
        if (file_extension == '.csv'):
            with open(full_path, newline='\n') as csv_file:
                csv_reader = csv.reader(csv_file)
                header = next(csv_reader)
                for col in header:
                    if col in dict_1:
                        dict_1[col].append(full_path)
                    else: 
                        dict_1[col] = [full_path]



## go through dictionary and check whether the files 
## that have the same header have the same data under
## that header
dict_2 = {}

for col in dict_1:
    for file in dict_1[col]:
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            index = header.index(col)

            all_blank = True
            col_data = [col]
            for row in csv_reader: 
                col_data.append(row[index])

                if row[index] != "":
                    all_blank = False

            if col in dict_2:
                if dict_2[col] != col_data:
                    print("the files have different data at column \"" + col + "\".")
            else:
                dict_2[col] = col_data

            if all_blank:
                print("\"" + file + "\"" + " has a blank row at i=" + str(index) + " (\"" + col + "\").")
