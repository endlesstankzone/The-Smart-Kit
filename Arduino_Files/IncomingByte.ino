int incomingByte = 0;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop(){
  
  if (Serial.available() > 0){
    
    incomingByte = Serial.read();
    
    Serial.print("I recieved: ");
    Serial.println(incomingByte, DEC);
    
    if (incomingByte == 79){
      digitalWrite(13, HIGH);
      Serial.println("on");
    } 
    if (incomingByte == 70){
      digitalWrite(13, LOW);
      Serial.println("off");
    } 
    
  }
}



