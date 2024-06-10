import serial
import time
import os
import random

os.system("clear")

ser = serial.Serial('/dev/cu.usbmodem11301', 115200)
# time.sleep(2)
#
# while ser.in_waiting > 0:
#     ser.readline()

number = random.randint(0,7)
# number = bin(number)
message = str(number)
ser.write(bytes(message + '\n\r', 'utf-8'))
time.sleep(0.05)

data = ser.readline().decode('utf-8').strip()
print(data)

time.sleep(0.05)

while True:
    data = ser.readline().decode('utf-8').strip()
    print(data)
    time.sleep(0.1)

ser.close()
