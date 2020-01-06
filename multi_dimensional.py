row_column = input()
num_rows = int(row_column.split()[0])
num_columns = int(row_column.split()[1])

#point: print list of rows as list of columns
list_of_rows = []

for i in range(num_rows):
    row_list = []
    row_list_input = input()
    for item in row_list_input.split():
        row_list.append(item)
    list_of_rows.append(row_list)

for i in range(num_columns):
    output_row = []
    for row in list_of_rows:
        output_row.append(row[i])
    print(" ".join(output_row))
