import os
import csv

rootdir = "/home/user/Desktop/sgsg/SAGA_Database/Headers"


## get a dictionary of all the headers connected to a list
## of the files that contain those headers
def get_files_with_header(rootdir):
    dict_1 = {}
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            full_path = os.path.join(subdir, file)
            #print(full_path)
            filename, file_extension = os.path.splitext(file)
            if (file_extension == '.csv'):
                with open(full_path, newline='\n', encoding="ANSI") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    header = next(csv_reader)
                    for col in header:
                        if col in dict_1:
                            dict_1[col].append(full_path)
                        else:
                            dict_1[col] = [full_path]
    return dict_1


## go through dictionary and check whether the files
## that have the same header have the same data under
## that header
def have_same_data(rootdir):
    dict_1 = get_files_with_header(rootdir)
    dict_2 = {}
    for col in dict_1:
        for file in dict_1[col]:
            with open(file, encoding="ANSI") as csv_file:
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

                #if all_blank:
                    #print("\"" + file + "\"" + " has a blank row at column \"" + col + "\".")
    return dict_2

def get_columns(dict_1):
    columns = []
    num_repeated_cols = 0
    for col in dict_1:
        columns.append(col)
        if len(dict_1[col]) > 1:
            num_repeated_cols = num_repeated_cols + 1
    return columns

#print("the columns are:")
#print(columns)

#print("there were " + str(num_repeated_cols) + " repeated column headers")
#print("there are " + str(len(columns)) + " total columns")

file_list = [".\\Turkey_4\\4 gesture description_1_a.code g2.csv",
    ".\\Turkey_4\\4 gesture description_2_b.g-sp list.csv",
    ".\\Turkey_4\\4 gesture description_3_2 all fields.csv",
    ".\\Turkey_4\\4 gesture description_4_a.code g-sp.csv",
    ".\\Turkey_4\\4 gesture description_5_c.create utts.csv",
    ".\\Turkey_4\\4 gesture description_6_d.questions.csv",
    ".\\Turkey_4\\4 gesture description_7_f.all fields.csv",
    ".\\Turkey_4\\4 gesture description_8_Layout #8.csv"
    ]

def get_columns(file_list):
    columns = set()
    for file in file_list:
        with open(file, encoding="ANSI") as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            for col in header:
                columns.add(col)
    return columns

## get number of non-blank rows
def get_number_nonblank(file_list):
    dict_3 = {}
    columns = get_columns(file_list)
    for col in columns:
        dict_4 = {}
        for file in file_list:
            with open(file, encoding="ANSI") as csv_file:
                csv_reader = csv.reader(csv_file)
                header = next(csv_reader)
                if col in header:
                    index = header.index(col)
                    num_non_blank = 0
                    for row in csv_reader:
                        if row[index] != "":
                            num_non_blank = num_non_blank + 1
                    dict_4[file] = num_non_blank
        dict_3[col] = dict_4
    return dict_3

def dict_to_csv(file_list):
    dict_3 = get_number_nonblank(file_list)
    f = open("number_nonblank.csv", "w")
    f.write(",")
    for file in file_list:
        f.write(file + ",")
    f.write("\n")
    for header in dict_3:
        f.write(header + ",")
        for file in file_list:
            if file in dict_3[header]:
                f.write(str(dict_3[header][file]) + ",")
            else:
                f.write(",")
        f.write("\n")

#dict_1 = get_files_with_header(rootdir)
#dict_2 = have_same_data(rootdir)
#columns = get_columns(dict_1)
#dict_3 = get_number_nonblank(file_list)
#print(dict_3)
dict_to_csv(file_list)
