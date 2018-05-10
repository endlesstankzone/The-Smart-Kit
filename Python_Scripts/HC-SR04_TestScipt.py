import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BCM)
ser = serial.Serial('/dev/ttyACM0',9600)

TRIG=23
ECHO=24

print("Distance Measurement In Progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting For Sensor to Settle")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)


while GPIO.input(ECHO) == 0:
    pulse_start = time.time()
    
while GPIO.input(ECHO) == 1:
    pulse_end = time.time()
    
pulse_duration=pulse_end-pulse_start
distance = pulse_duration*16500
distance = round(distance, 2)
print("Distance:", distance, "cm")
if distance < 15:
    ser.write("O".encode('utf-8'))
else:
    ser.write("F".encode('utf-8'))
GPIO.cleanup()





