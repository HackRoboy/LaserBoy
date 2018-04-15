#include <Wire.h>

#define SLAVE_ADDR 8

#include "XL320.h"

// Name your robot!
XL320 robot;

// If you want to use Software Serial, uncomment this line
#include <SoftwareSerial.h>

// Set the SoftwareSerial RX & TX pins
SoftwareSerial mySerial(10, 11); // (RX, TX)

// Set some variables for incrementing position & LED colour
char rgb[] = "rgbypcwo";

int servoID_V = 2;
int servoID_H = 4;
byte packet[4];

void setup() {
  // Serial Comm  
  Serial.begin(115200);           // start serial for output
  
  //Servos
  // Setup Software Serial
  mySerial.begin(115200);

  // Initialise your robot
  robot.Begin(mySerial); // Hand in the serial object you're using
  
  // I like fast moving servos, so set the joint speed to max!
  //robot.Write(2, XL320::Address::BAUD_RATE, 2);
  
  //I2C comm
  Wire.begin(SLAVE_ADDR);
  Wire.onReceive(receiveEvent);
  Serial.println("At the ready!");
  
}

void loop() {
  robot.Write(servoID_H, XL320::Address::LED, random(0,7) );
  delay(100);
  robot.Write(servoID_V, XL320::Address::LED, random(0,7) );
  delay(100);
}

void receiveEvent(int howMany) {
  Serial.println("Received something, let's see what it is");
  while (1 < Wire.available()) { // loop through all but the last
    //Serial.println(Wire.available());
    byte c = Wire.read(); // receive byte
    packet[Wire.available()] = c;
    Serial.print(c,HEX);         // print the byte
    Serial.print("\t");
  }
  byte x = Wire.read();    // receive byte as an integer
  packet[0] = x;
  Serial.println(x,HEX);         // print the integer
  for(int i=0;i<=2;i++){
    Serial.print(i);
    Serial.println(packet[i],HEX);
  }
  Serial.println(packet[3],HEX);
  
  short h_pos = 0x0000;
  short v_pos = 0x0000;

  v_pos = (packet[1] << 8) | packet[0];  // Calc vertical angle
  h_pos = (packet[3] << 8) | packet[2];  // Calc horizontal angle

  Serial.print("h_pos: ");
  Serial.println(h_pos);
  Serial.print("v_pos: ");
  Serial.println(v_pos);

  // Push angles to servos
  robot.Write(servoID_H, XL320::Address::GOAL_POSITION, h_pos );
  delay(100);
  robot.Write(servoID_V, XL320::Address::GOAL_POSITION, v_pos );
  delay(100);
}

