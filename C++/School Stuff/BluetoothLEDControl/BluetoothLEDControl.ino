//Code BY :
//Gary Khodayari
//16-10-2020
#include "BluetoothSerial.h" // ESP32 bluetooth Library
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED) // initial Config
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

extern int B, Y, R; // making integers responding to State value 
int BTorder; // bluetooth serial connection defining
BluetoothSerial SerialBT; // variable making


void setup() {
  Serial.begin(9600);
  pinMode (17, OUTPUT);
  pinMode (15, OUTPUT);
  pinMode (2, OUTPUT);
  SerialBT.begin("d0ntblink ESP-32"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
}

void loop() {
  if (SerialBT.available()) {
    BTorder = SerialBT.read();
    if ( BTorder == 'R') {
      SerialBT.println("Red LED changed state");
      // this part checks to see if the LED's Current state is HIGH or LOW
      if (digitalRead(17) == 0){ // if HIGH turns it LOW
        digitalWrite(17, HIGH); 
      } else { // if LOW turns it HIGH
        digitalWrite(17, LOW);
      }
    }
    if ( BTorder == 'B') {
      SerialBT.println("BLUE LED changed state");
      if (digitalRead(2) == 0){
        digitalWrite(2, HIGH);
      } else {
        digitalWrite(2, LOW);
      }
    }
    if ( BTorder == 'Y') {
      SerialBT.println("Yellow LED changed state");
      if (digitalRead(15) == 0){
        digitalWrite(15, HIGH);
      } else {
        digitalWrite(15, LOW);
      }
    }
    if ( BTorder == 'Q') {
      SerialBT.disconnect(); // Quits and disconnects
    }
  } 
}
