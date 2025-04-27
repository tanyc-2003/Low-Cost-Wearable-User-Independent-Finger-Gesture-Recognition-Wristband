import serial
import csv
import time
import re

# Set up 
PORT = 'COM3'  
BAUD_RATE = 115200
OUTPUT_FILE = 'File.csv'
set_number = 0


sPort = serial.Serial(PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Allow time for the connection to establish

# Signal ESP32 to start recording
while True:
    flag = True

    user_input = input("Press any key and Enter to start recording: ")

    if user_input != "": 
        sPort.write(b's')
        print("Signaled ESP32 to start recording...")

    # Receive data
    data = []
    while True:
        if sPort.in_waiting > 0:
            line = sPort.readline().decode('utf-8').strip()  # Read a line
            if line == "DONE":  # End of data transmission
                print("Data transmission complete.")
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
                    data.append(line)

            except ValueError:
                continue

    # Write data to CSV
    with open(OUTPUT_FILE, 'a+', newline='') as csvfile:

        print("Writting Data...")

        writer = csv.writer(csvfile)
        writer.writerow([', '.join(data)])

    print("Data recorded and saved")




