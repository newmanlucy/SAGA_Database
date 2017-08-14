file_list = "file_list.txt"	# file with list of csv files
curr_header = []		# main header
comp_header = []		# header compared with main header
list_files = []    		# list of csv files
list_headers = []		# list of different headers (list of list)
list_subset = []		# list of files with same header as curr_header

with open(file_list, 'r') as f, open(file_list, 'r') as f_files:
    for file_no, file_name in enumerate(f, start=0):
        file_name = file_name.strip()
        list_files.append(file_name)
        with open(file_name, 'r') as f_curr:
            curr_header = sorted(f_curr.readline().strip().split(','))
            if (curr_header not in list_headers):
                list_headers.append(curr_header)
                print("Header:\t" + str(curr_header))
                print("Files:\t"),
                f_files.seek(0)
                for i in xrange(file_no):
                    f_files.next()
                for line_comp in f_files:
                    line_comp = line_comp.strip()
                    with open(line_comp) as f_comp:
                        comp_header = sorted(f_comp.readline().strip().split(','))
                        if (curr_header == comp_header):
                            print(line_comp + ", "),
                print('\n')
