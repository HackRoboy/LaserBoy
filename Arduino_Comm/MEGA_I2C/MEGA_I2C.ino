#include <Wire.h>

#define MY_ADDR   // I2C address

#define 

void setup() {
  //Servos
  
  //I2C comm
  Wire.begin(MY_ADDR);
  Wire.onReceive(receiveEvent); // register event
  // Serial Comm
  Serial.begin(9600);           // start serial for output
}

void loop() {
  delay(100);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {
  while (1 < Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    Serial.print(c);         // print the character
  }
  int x = Wire.read();    // receive byte as an integer
  Serial.println(x); 
}