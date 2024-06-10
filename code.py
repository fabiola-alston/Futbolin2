import supervisor
import time
import board
import digitalio
import random


ledI1 = digitalio.DigitalInOut(board.GP28)
ledI1.direction = digitalio.Direction.OUTPUT

ledI2 = digitalio.DigitalInOut(board.GP5)
ledI2.direction = digitalio.Direction.OUTPUT

ledX1 = digitalio.DigitalInOut(board.GP27)
ledX1.direction = digitalio.Direction.OUTPUT

ledY1 = digitalio.DigitalInOut(board.GP26)
ledY1.direction = digitalio.Direction.OUTPUT

ledZ1 = digitalio.DigitalInOut(board.GP22)
ledZ1.direction = digitalio.Direction.OUTPUT

ledX2 = digitalio.DigitalInOut(board.GP8)
ledX2.direction = digitalio.Direction.OUTPUT

ledY2 = digitalio.DigitalInOut(board.GP7)
ledY2.direction = digitalio.Direction.OUTPUT

ledZ2 = digitalio.DigitalInOut(board.GP6)
ledZ2.direction = digitalio.Direction.OUTPUT

A = digitalio.DigitalInOut(board.GP11)
A.direction = digitalio.Direction.OUTPUT

B = digitalio.DigitalInOut(board.GP12)
B.direction = digitalio.Direction.OUTPUT

C = digitalio.DigitalInOut(board.GP13)
C.direction = digitalio.Direction.OUTPUT

X = digitalio.DigitalInOut(board.GP20)
X.direction = digitalio.Direction.INPUT

Y = digitalio.DigitalInOut(board.GP19)
Y.direction = digitalio.Direction.INPUT

Z = digitalio.DigitalInOut(board.GP18)
Z.direction = digitalio.Direction.INPUT        


def turnOffAll():
    ledX1.value = False
    ledY1.value = False
    ledZ1.value = False
    ledX2.value = False
    ledY2.value = False
    ledZ2.value = False
    
team = 1
    
def subtraction():
    if team == 1:
        ledX1.value = X.value
        ledY1.value = Y.value
        ledZ1.value = Z.value
    if team == 2:
        ledX2.value = X.value
        ledY2.value = Y.value
        ledZ2.value = Z.value
        
    
while True:
    if supervisor.runtime.serial_bytes_available:
        turnOffAll()
        value = input().strip()
        print(f"Received: {value}\r")
      
        if value == "0":
            A.value = 0
            B.value = 0
            C.value = 0
            print("5\r")
            
        elif value == "1":
            A.value = 0
            B.value = 0
            C.value = 1
            print("6\r")
            
        elif value == "2":
            A.value = 0
            B.value = 1
            C.value = 0
            print("7\r")
        
        elif value == "3":
            A.value = 0
            B.value = 1
            C.value = 1
            print("0\r")
            
        elif value == "4":
            A.value = 1
            B.value = 0
            C.value = 0
            print("1\r")
            
        elif value == "5":
            A.value = 1
            B.value = 0
            C.value = 1
            print("2\r")
            
        elif value == "6":
            A.value = 1
            B.value = 1
            C.value = 0
            print("3\r")
            
        elif value == "7":
            A.value = 1
            B.value = 1
            C.value = 1
            print("4\r")
        
    team = random.randint(1,2)
    
    
    subtraction()
    
    
    time.sleep(0.5)
    



        