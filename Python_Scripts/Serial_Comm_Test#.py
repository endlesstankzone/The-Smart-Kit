import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
#while True:
ser.write("f".encode('utf-8'))
time.sleep(2)  
ser.write("b".encode('utf-8'))
time.sleep(2) 
ser.write("r".encode('utf-8'))
time.sleep(2)  
ser.write("l".encode('utf-8'))
time.sleep(2)
ser.write("s".encode('utf-8'))
time.sleep(2) 
	
	
	
