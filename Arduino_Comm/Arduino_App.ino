#include <ESP8266WiFi.h>
#include <ESP8266WiFiAP.h>
#include <ESP8266WiFiGeneric.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266WiFiScan.h>
#include <ESP8266WiFiSTA.h>
#include <ESP8266WiFiType.h>
#include <WiFiClient.h>
#include <WiFiClientSecure.h>
#include <WiFiServer.h>
#include <WiFiServerSecure.h>
#include <WiFiUdp.h>

char incomingPacket[255];
WiFiUDP myUDP;

void setup()
{
  Serial.begin(115200);
  Serial.println();

  Serial.println("Wifi-Test");

  WiFi.begin("UnternehmerTUM", "");

  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());


//UDP setup
  
  unsigned int port = 4210;
 

  myUDP.begin(port);


}

void loop() {
  // put your main code here, to run repeatedly:
  //listen for udp
  int packetSize = myUDP.parsePacket();
  if (packetSize)
  {
    Serial.printf("Received %d bytes from %s, port %d\n", packetSize, myUDP.remoteIP().toString().c_str(), myUDP.remotePort());
    //read the incoming message
    int len = myUDP.read(incomingPacket, 255);
    if (len > 0)
    {
    incomingPacket[len] = 0;
    }
    Serial.printf("UDP packet contents: %s\n", incomingPacket, HEX);

    byte angle_phi = incomingPacket[0];
    byte angle_delta = incomingPacket[1];

    Serial.printf("Phi is %d\n", angle_phi);
    Serial.printf("Delta is %d\n", angle_delta);
  }


}