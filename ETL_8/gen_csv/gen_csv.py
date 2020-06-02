import csv

def write_csv(csv_path,row_list):
    with open(csv_path, 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

def add_row(row_list, str1, str2):

    row_list.append([str1,str2])

    return row_list