import csv

INPUT_FILE = 'MyOK2.csv'
OUTPUT_FILE = 'EMG_Data_MyOK2.csv'

window_size = 1000
overlap = 200

data = []
number_window = 0
col_start = 0
col_end = window_size

try:

    with open(INPUT_FILE, 'r', newline='') as file:
        reader = csv.reader(file)

        for i, row in enumerate(reader):
            col_start = 0
            col_end = window_size
            number_of_window = (len(row)-window_size)/(window_size-overlap) + 1

            for j in range (int(number_of_window)):
                extracted_colums = row[col_start:col_end]
                data.append(extracted_colums)

                col_start = col_end - overlap
                col_end = col_start + window_size


    with open(OUTPUT_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


    print(f"Data successfully extracted and appended to {OUTPUT_FILE}.")
    
except Exception as e:
    print(f"An error occurred: {e}")

