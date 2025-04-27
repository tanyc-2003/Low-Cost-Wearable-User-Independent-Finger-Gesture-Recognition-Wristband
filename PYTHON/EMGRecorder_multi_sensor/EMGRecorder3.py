import serial
import csv
import time
import re
import struct

# Set up 
PORT = 'COM4'  
BAUD_RATE = 115200
OUTPUT_FILE1 = 'Subject12/Data/Gesture0_CH1.csv'
OUTPUT_FILE2 = 'Subject12/Data/Gesture0_CH2.csv'
OUTPUT_FILE3 = 'Subject12/Data/Gesture0_CH3.csv'
NUM_SAMPLES = 5000  # Number of samples per channel

sPort = serial.Serial(PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Allow time for the connection to establish

# Signal ESP32 to start recording
while True:
    flag = True
    channel = 0

    user_input = input("Press any key and Enter to start recording: ")

    if user_input != "": 
        sPort.write(b'a')
        print("Signaled ESP32 to start recording...")

    # Receive data
    data1 = []
    data2 = []
    data3 = []

    time.sleep(1)  # Allow time for the sPort to clear

    ############## CHANNEL 1 ##############
    while True:
        if sPort.in_waiting > 0:
            line = sPort.readline().decode('utf-8').strip()  # Read a line
            
            if line == "DONE":  # End of data colleciton

                print("Receiving Channel 1 data...")

                # Read binary data
                binary_data = sPort.read(NUM_SAMPLES * 2)  # Read 5000 uint16_t values (2 bytes each)
                if len(binary_data) == NUM_SAMPLES * 2:
                    # Unpack binary data into a list of integers
                    data1 = list(struct.unpack(f'{NUM_SAMPLES}H', binary_data))  # 'H' for uint16_t
                    print("Channel 1 data received.")

                    # Write data to CSV
                    with open(OUTPUT_FILE1, 'a+', newline='') as csvfile:
                        print("Writing Channel 1 Data...")
                        writer = csv.writer(csvfile)
                        writer.writerow(data1)  # Write the list of integers as a row

                    print("Channel 1 data recorded and saved.")

                    sPort.write(b'b')  # Send acknowledgment to ESP32
                    time.sleep(2)
                else:
                    print("Error: Incomplete data received for Channel 1.")
                    print(f"Error: Expected {NUM_SAMPLES * 2} bytes, got {len(binary_data)} bytes.")



                ############## CHANNEL 2 ##############

                print("Receiving Channel 2 data...")

                # Read binary data
                binary_data = sPort.read(NUM_SAMPLES * 2)  # Read 5000 uint16_t values (2 bytes each)
                if len(binary_data) == NUM_SAMPLES * 2:
                    # Unpack binary data into a list of integers
                    data2 = list(struct.unpack(f'{NUM_SAMPLES}H', binary_data))  # 'H' for uint16_t
                    print("Channel 2 data received.")

                    # Write data to CSV
                    with open(OUTPUT_FILE2, 'a+', newline='') as csvfile:
                        print("Writing Channel 2 Data...")
                        writer = csv.writer(csvfile)
                        writer.writerow(data2)  # Write the list of integers as a row

                    print("Channel 2 data recorded and saved.")

                    sPort.write(b'c')  # Send acknowledgment to ESP32
                    time.sleep(2)
                else:
                    print("Error: Incomplete data received for Channel 2.")

                        


                ############## CHANNEL 3 ##############

                print("Receiving Channel 3 data...")

                # Read binary data
                binary_data = sPort.read(NUM_SAMPLES * 2)  # Read 5000 uint16_t values (2 bytes each)
                if len(binary_data) == NUM_SAMPLES * 2:
                    # Unpack binary data into a list of integers
                    data3 = list(struct.unpack(f'{NUM_SAMPLES}H', binary_data))  # 'H' for uint16_t
                    print("Channel 3 data received.")

                    # Write data to CSV
                    with open(OUTPUT_FILE3, 'a+', newline='') as csvfile:
                        print("Writing Channel 3 Data...")
                        writer = csv.writer(csvfile)
                        writer.writerow(data3)  # Write the list of integers as a row

                    print("Channel 3 data recorded and saved.")
                    break

                else:
                    print("Error: Incomplete data received for Channel 3.")





