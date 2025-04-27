import csv


S = '13'

INPUT_FILE_0_1 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture0_CH1.csv'
INPUT_FILE_0_2 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture0_CH2.csv'
INPUT_FILE_0_3 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture0_CH3.csv'

INPUT_FILE_1_1 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture1_CH1.csv'
INPUT_FILE_1_2 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture1_CH2.csv'
INPUT_FILE_1_3 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture1_CH3.csv'

INPUT_FILE_2_1 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture2_CH1.csv'
INPUT_FILE_2_2 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture2_CH2.csv'
INPUT_FILE_2_3 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture2_CH3.csv'

INPUT_FILE_3_1 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture3_CH1.csv'
INPUT_FILE_3_2 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture3_CH2.csv'
INPUT_FILE_3_3 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture3_CH3.csv'

INPUT_FILE_4_1 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture4_CH1.csv'
INPUT_FILE_4_2 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture4_CH2.csv'
INPUT_FILE_4_3 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture4_CH3.csv'

INPUT_FILE_5_1 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture5_CH1.csv'
INPUT_FILE_5_2 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture5_CH2.csv'
INPUT_FILE_5_3 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture5_CH3.csv'

INPUT_FILE_6_1 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture6_CH1.csv'
INPUT_FILE_6_2 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture6_CH2.csv'
INPUT_FILE_6_3 = f'Subject{S}/500ms_Window/DATA_Windowed/Windowed_Gesture6_CH3.csv'


OUTPUT_FILE_0 = f'Subject{S}/500ms_Window/EMG_DATA_Chained/EMG_DATA_Gesture0_S{S}_500ms.csv'
OUTPUT_FILE_1 = f'Subject{S}/500ms_Window/EMG_DATA_Chained/EMG_DATA_Gesture1_S{S}_500ms.csv'
OUTPUT_FILE_2 = f'Subject{S}/500ms_Window/EMG_DATA_Chained/EMG_DATA_Gesture2_S{S}_500ms.csv'
OUTPUT_FILE_3 = f'Subject{S}/500ms_Window/EMG_DATA_Chained/EMG_DATA_Gesture3_S{S}_500ms.csv'
OUTPUT_FILE_4 = f'Subject{S}/500ms_Window/EMG_DATA_Chained/EMG_DATA_Gesture4_S{S}_500ms.csv'
OUTPUT_FILE_5 = f'Subject{S}/500ms_Window/EMG_DATA_Chained/EMG_DATA_Gesture5_S{S}_500ms.csv'
OUTPUT_FILE_6 = f'Subject{S}/500ms_Window/EMG_DATA_Chained/EMG_DATA_Gesture6_S{S}_500ms.csv'

def chain(input_file_1, input_file_2, input_file_3, output_file):
    # Open all input files and the output file
    with open(input_file_1, 'r') as file1, open(input_file_2, 'r') as file2, open(input_file_3, 'r') as file3, open(output_file, 'w', newline='') as outfile:
        reader1 = csv.reader(file1)
        reader2 = csv.reader(file2)
        reader3 = csv.reader(file3)
        writer = csv.writer(outfile)

        # Iterate through all files row by row
        for row1, row2, row3 in zip(reader1, reader2, reader3):
            writer.writerow(row1 + row2 + row3)  # Concatenate rows and write

chain(INPUT_FILE_0_1, INPUT_FILE_0_2, INPUT_FILE_0_3, OUTPUT_FILE_0)
chain(INPUT_FILE_1_1, INPUT_FILE_1_2, INPUT_FILE_1_3, OUTPUT_FILE_1)
chain(INPUT_FILE_2_1, INPUT_FILE_2_2, INPUT_FILE_2_3, OUTPUT_FILE_2)
chain(INPUT_FILE_3_1, INPUT_FILE_3_2, INPUT_FILE_3_3, OUTPUT_FILE_3)
chain(INPUT_FILE_4_1, INPUT_FILE_4_2, INPUT_FILE_4_3, OUTPUT_FILE_4)
chain(INPUT_FILE_5_1, INPUT_FILE_5_2, INPUT_FILE_5_3, OUTPUT_FILE_5)
chain(INPUT_FILE_6_1, INPUT_FILE_6_2, INPUT_FILE_6_3, OUTPUT_FILE_6)


