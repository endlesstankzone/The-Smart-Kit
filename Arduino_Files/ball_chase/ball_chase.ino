#include <Servo.h>

int value = 1500;

Servo leftEsc, rightEsc;

int incomingByte = 0;

void setup(){
  leftEsc.attach(5);
  rightEsc.attach(3);
  Serial.begin(57600);
  leftEsc.writeMicroseconds(value);
  rightEsc.writeMicroseconds(value);
  delay(5000);
}

void loop(){
  
  if (Serial.available() > 0){
    
    incomingByte = Serial.read();
    //Serial.print("I recieved: ");
    //Serial.println(incomingByte, DEC);
    
    if (incomingByte == 102){
      leftEsc.writeMicroseconds(1400);
      rightEsc.writeMicroseconds(1600);       
    }
    
    if (incomingByte == 98){
      leftEsc.writeMicroseconds(1600);
      rightEsc.writeMicroseconds(1400);
    }
    
    if (incomingByte == 115){
      leftEsc.writeMicroseconds(1500);
      rightEsc.writeMicroseconds(1500);
    }
    
    if (incomingByte == 108){
      leftEsc.writeMicroseconds(1600);
      rightEsc.writeMicroseconds(1600);
    }
    
    if (incomingByte == 114){
      leftEsc.writeMicroseconds(1400);
      rightEsc.writeMicroseconds(1400);
    }
  }
  
}
    
        
    


