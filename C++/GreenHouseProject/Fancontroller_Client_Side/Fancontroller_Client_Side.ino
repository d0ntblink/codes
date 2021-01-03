/*------------------------------------------------------------------------------ 
  Humidity and Temprature sensor with Server side Communication 
  Coded By : Gary. K
  Language : C++
  Platform : Arduino/ESP8266
  ------------------------------------------------------------------------------
  Parts :
    DHT22 , ESP8266 , RED LED , BLUE LED , 1000 OHM RESISTOR ,
    330 OHM RESISTOR x2 , BUZZER , DS3231 , 5/12V FAN , MOSFET ,
    GAUGE 8 WIRES
  ------------------------------------------------------------------------------
  Description : 
    ESP8266 is set to read humidity and temprature data from a DHTSensor, sync it
    with real world datetime and send it to a server to be accessed from anywhere.
  ------------------------------------------------------------------------------
  Troubleshooting LED Code L00Ps :
  REDshort --> REDlong --> REDshort = POST failed
  BLUElong = POST successfull
  BLUElong --> REDlong = Attempting to connect to WiFi
  ------------------------------------------------------------------------------
  /////////d0ntblink\\\\\\\\\\\
  \\\\www.dontblink.ca////
  ------------------------------------------------------------------------------*/

// Liberaries //
#include <DHT.h>
#include <MapFloat.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include <Wire.h>
#include <RTClib.h>
#include <string>
#include <ArduinoJson.h>

// Constants //
#define FANPIN  D4
#define DHTPIN 14     // what digital pin we're connected to
#define DHTTYPE DHT22   // DHT 22
#define red 13  //rest of the pins (LED + BUZZER)
#define blue 12
#define buzzer 15
char ssid[] = "SSID NAME";
char password[] =  "WIFI PASSWORD";
char host[] = "SERVER IP/DOMAIN NAME";

// Setup Requirements //
DHT dht(DHTPIN, DHTTYPE); //Initialize DHT sensor for normal 16mhz Arduino
RTC_DS3231 rtc; //function rename for ease of use
WiFiClient client; //function rename for ease of use

// Variables //
int pwmlowlimit = 400.00; //LRV and URV for PWM
int pwmhighlimit = 1023.00; //change this based on your board
int templowlimit = 25.00;   //LRV AND URV for temprature
int temphighlimit = 30.00;
float hum, temp, tempmap, volt; //FLOAT vairables
int PWMVal;
int hh=0,mm=0; //datetime reset
String curtime, postData, curdate, datetime, datetimeData, tempData, humData, fanData, httpCode, serveResponse; //Strings creation

// SETUP START //
void setup() {
  // Pin Setups //
  pinMode (FANPIN, OUTPUT); // I/O setup for components
  pinMode (red, OUTPUT);
  pinMode (blue, OUTPUT);
  pinMode (buzzer, OUTPUT);
  pinMode (DHTPIN, INPUT);
  Serial.begin(115200); // Serial port baud rate 
  Wire.begin(); // RTC connect
  rtc.begin();
  dht.begin(); // DHT connect


  // RTC Time Sync //
  rtc.adjust(DateTime(F(__DATE__),F(__TIME__))); // GRABS DATE TIME FROM PC WHEN COMPILED

  // WiFi Setup //
  WiFi.mode(WIFI_STA);        //This line hides the viewing of ESP as wifi hotspot
  WiFi.begin(ssid, password);  //Connect to the WiFi network
  while (WiFi.status() != WL_CONNECTED) {  //Wait for connection
    Serial.println("Attempting to connect to WiFi..."); 
    digitalWrite(blue, HIGH); //LED LOOP FOR PHYSICAL CODE
    delay(500);
    digitalWrite(blue, LOW);
    delay(500);
    digitalWrite(red, HIGH);
    delay(500);
    digitalWrite(red, LOW);
    delay(500);
  }

  // WiFi Info Serial Print Out //
  Serial.print("******************************************");
  Serial.print("\nCurrentIP address : ");
  Serial.println(WiFi.localIP());  //Print the local IP
  Serial.print("Connected to : ");
  Serial.println(WiFi.SSID()); //Print SSID
  Serial.print("My Doorway to the World Wide Web : ");
  Serial.println(WiFi.gatewayIP()); //Print Gateway
  Serial.print("******************************************\n");

}

// L00P START //
void loop() {
  DateTime now = rtc.now(); //REAL TIME CLOCK FUNCTION GRAB

  // Reading DH22 Data //
  hum = dht.readHumidity(); //RENAME FOR EASE OF USE
  temp= dht.readTemperature();

  // Setting Alarm staus //
  if ( temp > temphighlimit){ //IF/ELSE TEMP CHECK PROCESSING
    tempmap = temphighlimit;
    digitalWrite(red, HIGH);
    tone(buzzer, 1000, 200);
  } else if (temp < templowlimit) { //SETTING THE RED LED ON/OFF
    tempmap = templowlimit;
    digitalWrite(red, LOW);
    noTone(buzzer);
  } else {
    tempmap = temp;
    digitalWrite(red, LOW);
    noTone(buzzer);
  }

  // Fan Voltage and PWM Calculation //
  PWMVal = mapFloat(tempmap, templowlimit, temphighlimit, pwmlowlimit, pwmhighlimit);
  volt = mapFloat(PWMVal, 0.00, 1024.00, 0.00, 5.00);
  analogWrite(FANPIN, PWMVal);

  // POST Setup //
  curtime = F("");
  curdate = F("");
  datetime = F("");
  //------- making a time string
  curtime += String(now.hour(), DEC);
  curtime += F(":");
  curtime += String(now.minute(), DEC);
  curtime += F(":");
  curtime += String(now.second(), DEC);
  //-------- making a date string
  curdate += String(now.year(), DEC);
  curdate += F("-");
  curdate += String(now.month(), DEC);
  curdate += F("-");
  curdate += String(now.day(), DEC);
  //-------- making one date time 
  datetime = curdate + " " + curtime;
  //-------- creating an array payload
  postData = "temp=" + String(temp) + "&hum=" + String(hum) + "&volt=" + String(volt) + "&DT=" + datetime;

  
  // Webserver POST request //
  HTTPClient http;
  http.begin("php page address");              //Specify request destination
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");    //Specify content-type header
  httpCode = String(http.POST(postData));
  serveResponse = http.getString();    //Get the response payload
  http.end();  //Close connection
  if (httpCode == "200") {  //check if the POST was successfull
      Serial.print("\n");
      Serial.print("\npayload sent successfully...\n");
      digitalWrite(blue, HIGH);
      delay(500);
      digitalWrite(blue, LOW);
      delay(500);
  } else { //incase of a post failiure red led will blink 3 times then go back to its last state as well as the a debugging serial prot notice
    Serial.print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
    Serial.print("\n!!!!!!!!!POST request failed!!!!!!!!!!!!\n");
    Serial.print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
    if (digitalRead(red) == 0) {  //Creating a physically visible failiure code
      digitalWrite(red, HIGH);
      delay(100);
      digitalWrite(red, LOW);
      delay(100);
      digitalWrite(red, HIGH);
      delay(500);
      digitalWrite(red, LOW);
      delay(100);
      digitalWrite(red, HIGH);
      delay(100);
      digitalWrite(red, LOW);
    } else {
      digitalWrite(red, LOW);
      delay(100);
      digitalWrite(red, HIGH);
      delay(100);
      digitalWrite(red, LOW);
      delay(100);
      digitalWrite(red, HIGH);
      delay(500);
      digitalWrite(red, LOW);
      delay(100);
      digitalWrite(red, HIGH);
    }
  }
  if (client.connected()) { //Did I sed it ? 
    client.stop();
    digitalWrite(blue, LOW); //Show the post was succesfull
    Serial.print("\n");
  }

  
  // Debugging Serial OUTPUTS //
  Serial.print("Datetime: ");
  Serial.println(datetime);
  Serial.print("POST Code: ");
  Serial.println(httpCode);
  Serial.print("Temprature: ");
  Serial.println(temp);
  Serial.print("Humidity %: ");
  Serial.println(hum);
  Serial.print("PWM rate: ");
  Serial.println(PWMVal);
  Serial.print("Fan Voltage: ");
  Serial.println(volt);
  Serial.print("POST data: ");
  Serial.println(postData);
  Serial.print("Server Response: ");
  Serial.println(serveResponse);
  Serial.print("\n------------------------------------------------------------------------\n");

  // FINAL DELAY //
  delay(5000);
}
