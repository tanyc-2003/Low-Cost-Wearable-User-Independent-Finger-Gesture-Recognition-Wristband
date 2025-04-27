import serial
import csv
import time
import re
import struct

# Set up 

PORT = 'COM4'  
BAUD_RATE = 115200
OUTPUT_FILE1 = 'Gesture6_CH1.csv'
OUTPUT_FILE2 = 'Gesture6_CH2.csv'
OUTPUT_FILE3 = 'Gesture6_CH3.csv'
set_number = 0


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
            
            if line == "DONE":  # End of data transmission
                print("Channel 1 data transmission complete.")

                # Write data to CSV
                with open(OUTPUT_FILE1, 'a+', newline='') as csvfile:

                    print("Writting Channel 1 Data...")

                    writer = csv.writer(csvfile)
                    writer.writerow([', '.join(data1)])

                print("Channel 1 data recorded and saved")

                sPort.write(b'b')
                flag = True
                break

            try:
                if flag:
                    print("Data transmitting...")
                    flag = False
                
                # Extract only numeric parts using a regular expression
                # Regular Expression (r'\d+'): \d+ matches sequences of digits in the string.
                # re.findall: Extracts all matching sequences (numeric portions) from the string.
                numbers = re.findall(r'\d+', line)
                if numbers:  # If numeric parts are found
                    data1.append(line)

            except ValueError:
                continue



    ############## CHANNEL 2 ##############

    while True:
        if sPort.in_waiting > 0:
            line = sPort.readline().decode('utf-8').strip()  # Read a line
            
            if line == "DONE":  # End of data transmission
                print("Channel 2 data transmission complete.")

                # Write data to CSV
                with open(OUTPUT_FILE2, 'a+', newline='') as csvfile:

                    print("Writting Channel 2 Data...")

                    writer = csv.writer(csvfile)
                    writer.writerow([', '.join(data2)])

                print("Channel 2 data recorded and saved")

                sPort.write(b'c')
                flag = True
                break

            try:
                if flag:
                    print("Data transmitting...")
                    flag = False
                
                # Extract only numeric parts using a regular expression
                # Regular Expression (r'\d+'): \d+ matches sequences of digits in the string.
                # re.findall: Extracts all matching sequences (numeric portions) from the string.
                numbers = re.findall(r'\d+', line)
                if numbers:  # If numeric parts are found
                    data2.append(line)

            except ValueError:
                continue

            


    ############## CHANNEL 3 ##############

    while True:
        if sPort.in_waiting > 0:
            line = sPort.readline().decode('utf-8').strip()  # Read a line
            
            if line == "DONE":  # End of data transmission
                print("Channel 3 data transmission complete.")

                # Write data to CSV
                with open(OUTPUT_FILE3, 'a+', newline='') as csvfile:

                    print("Writting Channel 3 Data...")

                    writer = csv.writer(csvfile)
                    writer.writerow([', '.join(data3)])

                print("Channel 3 data recorded and saved")

                break

            try:
                if flag:
                    print("Data transmitting...")
                    flag = False
                
                # Extract only numeric parts using a regular expression
                # Regular Expression (r'\d+'): \d+ matches sequences of digits in the string.
                # re.findall: Extracts all matching sequences (numeric portions) from the string.
                numbers = re.findall(r'\d+', line)
                if numbers:  # If numeric parts are found
                    data3.append(line)

            except ValueError:
                continue

            






