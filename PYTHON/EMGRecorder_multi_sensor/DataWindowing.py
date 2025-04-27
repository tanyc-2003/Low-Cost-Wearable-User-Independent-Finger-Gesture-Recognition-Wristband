import csv

Subject = 'Subject13'


INPUT_FILE_0_1 = f'{Subject}/Data/Gesture0_CH1.csv'
INPUT_FILE_0_2 = f'{Subject}/Data/Gesture0_CH2.csv'
INPUT_FILE_0_3 = f'{Subject}/Data/Gesture0_CH3.csv'
 
INPUT_FILE_1_1 = f'{Subject}/Data/Gesture1_CH1.csv'
INPUT_FILE_1_2 = f'{Subject}/Data/Gesture1_CH2.csv'
INPUT_FILE_1_3 = f'{Subject}/Data/Gesture1_CH3.csv'
 
INPUT_FILE_2_1 = f'{Subject}/Data/Gesture3_CH1.csv'
INPUT_FILE_2_2 = f'{Subject}/Data/Gesture3_CH2.csv'
INPUT_FILE_2_3 = f'{Subject}/Data/Gesture3_CH3.csv'
 
INPUT_FILE_3_1 = f'{Subject}/Data/Gesture3_CH1.csv'
INPUT_FILE_3_2 = f'{Subject}/Data/Gesture3_CH2.csv'
INPUT_FILE_3_3 = f'{Subject}/Data/Gesture3_CH3.csv'
 
INPUT_FILE_4_1 = f'{Subject}/Data/Gesture4_CH1.csv'
INPUT_FILE_4_2 = f'{Subject}/Data/Gesture4_CH2.csv'
INPUT_FILE_4_3 = f'{Subject}/Data/Gesture4_CH3.csv'
 
INPUT_FILE_5_1 = f'{Subject}/Data/Gesture5_CH1.csv'
INPUT_FILE_5_2 = f'{Subject}/Data/Gesture5_CH2.csv'
INPUT_FILE_5_3 = f'{Subject}/Data/Gesture5_CH3.csv'
 
INPUT_FILE_6_1 = f'{Subject}/Data/Gesture6_CH1.csv'
INPUT_FILE_6_2 = f'{Subject}/Data/Gesture6_CH2.csv'
INPUT_FILE_6_3 = f'{Subject}/Data/Gesture6_CH3.csv'
 

OUTPUT_FILE_0_1 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture0_CH1.csv'
OUTPUT_FILE_0_2 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture0_CH2.csv'
OUTPUT_FILE_0_3 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture0_CH3.csv'
 
OUTPUT_FILE_1_1 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture1_CH1.csv'
OUTPUT_FILE_1_2 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture1_CH2.csv'
OUTPUT_FILE_1_3 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture1_CH3.csv'
 
OUTPUT_FILE_2_1 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture2_CH1.csv'
OUTPUT_FILE_2_2 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture2_CH2.csv'
OUTPUT_FILE_2_3 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture2_CH3.csv'
 
OUTPUT_FILE_3_1 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture3_CH1.csv'
OUTPUT_FILE_3_2 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture3_CH2.csv'
OUTPUT_FILE_3_3 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture3_CH3.csv'
 
OUTPUT_FILE_4_1 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture4_CH1.csv'
OUTPUT_FILE_4_2 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture4_CH2.csv'
OUTPUT_FILE_4_3 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture4_CH3.csv'
 
OUTPUT_FILE_5_1 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture5_CH1.csv'
OUTPUT_FILE_5_2 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture5_CH2.csv'
OUTPUT_FILE_5_3 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture5_CH3.csv'
 
OUTPUT_FILE_6_1 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture6_CH1.csv'
OUTPUT_FILE_6_2 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture6_CH2.csv'
OUTPUT_FILE_6_3 = f'{Subject}/500ms_Window/DATA_Windowed/Windowed_Gesture6_CH3.csv'
 


window_size = 250
overlap = 50


number_window = 0
col_start = 0
col_end = window_size



for n in range(7):
    for m in range(3):

        data = []
        
        input_file = globals()[f"INPUT_FILE_{n}_{m+1}"]
        output_file = globals()[f"OUTPUT_FILE_{n}_{m+1}"]
        
        try:

            with open(input_file, 'r', newline='') as file:
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


            with open(output_file, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)


            print(f"Data successfully extracted and appended to {output_file}.")
            
        except Exception as e:
            print(f"An error occurred: {e}")

