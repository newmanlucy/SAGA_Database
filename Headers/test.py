import csv

toCSV = [{"tester": 1, "testers": 2},{"tester": 14, "testernn": 28}]
keys = toCSV[0].keys()

with open('people.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)
