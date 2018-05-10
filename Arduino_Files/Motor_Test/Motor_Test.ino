#include <Servo.h>

int value = 1500;

Servo leftEsc, rightEsc;

void setup(){
  leftEsc.attach(5);
  rightEsc.attach(3);
  Serial.begin(9600);
  leftEsc.writeMicroseconds(value);
  rightEsc.writeMicroseconds(value);
  delay(5000);
}


void loop(){
  
  leftEsc.writeMicroseconds(1200);
  //rightEsc.writeMicroseconds(1200);
  delay(1000);
  leftEsc.writeMicroseconds(1500);
  //rightEsc.writeMicroseconds(1500);
  delay(1000);
  leftEsc.writeMicroseconds(1800);
  //rightEsc.writeMicroseconds(1800);
  delay(1000);
  leftEsc.writeMicroseconds(1500);
  //rightEsc.writeMicroseconds(1500);
  delay(1000);
}

  
