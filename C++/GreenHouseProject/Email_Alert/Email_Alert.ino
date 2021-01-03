put #include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <iostream>
#include <string>

// Constants
const char* ssid = "SSID";
const char* password = "WIFI PASSWORD";
char server[] = "mail.smtp2go.com"; // The SMTP Server  ( CAN BE OTHER MAIL SERVICES IF U WANT)

// Variables
String payload;
float fpayload;

WiFiClient espClient;
void setup () {
  Serial.begin(115200);
  // WiFi Setup //
  WiFi.mode(WIFI_STA);        //This line hides the viewing of ESP as wifi hotspot
  WiFi.begin(ssid, password);  //Connect to the WiFi network
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print("Connecting..\n");
  }
}
 
void loop() {
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    HTTPClient http;  //Declare an object of class HTTPClient
    http.begin("POST PAGE");  //Specify request destination
    int httpCode = http.GET();                                                                  //Send the request
    if (httpCode > 0) { //Check the returning code
      payload = http.getString();   //Get the request response payload
      Serial.println(payload);   
      delay(1000);//Print the response payload
    }
    http.end();   //Close connection
  }

  fpayload = payload.toFloat();
  if ( fpayload > 30.0 ) {
  byte ret = sendEmail();
  } else {
  Serial.println("No email alarm was sent");
  }
  delay(20000);
}


byte sendEmail() {
  if (espClient.connect(server, 2525) == 1) {
    Serial.println(F("connected"));
  } 
  else {
    Serial.println(F("connection failed"));
    return 0;
  }
  if (!emailResp()) 
    return 0;
  //
  Serial.println(F("Sending EHLO"));
  espClient.println("EHLO www.example.com");
  if (!emailResp()) 
    return 0;
  //  
  Serial.println(F("Sending auth login"));
  espClient.println("AUTH LOGIN");
  if (!emailResp()) 
    return 0;
  //  
  Serial.println(F("Sending User")); // Change this to your base64, ASCII encoded username
  espClient.println("USERNAME IN BASE64"); //base64, ASCII encoded Username
  if (!emailResp()) 
    return 0;
  //
  Serial.println(F("Sending Password")); // change to your base64, ASCII encoded password
  espClient.println("PASSWORD IN BASE64");//base64, ASCII encoded Password
  if (!emailResp()) 
    return 0;
  //
  Serial.println(F("Sending From"));
  // change to sender email address
  espClient.println(F("MAIL From: TempratureAlertRobot@gmail.com"));
  if (!emailResp()) 
    return 0;
  // change to recipient address
  Serial.println(F("Sending To"));
  espClient.println(F("RCPT To: <RECIEVER EMAIL>"));
  if (!emailResp()) 
    return 0;
  //
  Serial.println(F("Sending DATA"));
  espClient.println(F("DATA"));
  if (!emailResp()) 
    return 0;
  Serial.println(F("Sending email"));
  // change to recipient address
  espClient.println(F("To:  <RECIEVER EMAIL>"));
  // change to your address
  espClient.println(F("From: <SENDER EMAIL>"));
  espClient.println(F("Subject: ESP8266 test e-mail\r\n"));
  espClient.println(F("temprature readings are high\n"));
  espClient.println(F("Please take care of it."));
  //
  espClient.println(F("."));
  if (!emailResp()) 
    return 0;
  //
  Serial.println(F("Sending QUIT"));
  espClient.println(F("QUIT"));
  if (!emailResp()) 
    return 0;
  //
  espClient.stop();
  Serial.println(F("disconnected"));
  return 1;
}
byte emailResp(){
  byte responseCode;
  byte readByte;
  int loopCount = 0;
  while (!espClient.available()) {
    delay(1);
    loopCount++;  // Wait for 20 seconds and if nothing is received, stop.
    if (loopCount > 20000) {
      espClient.stop();
      Serial.println(F("\r\nTimeout"));
      return 0;
    }
  }
  responseCode = espClient.peek();
  while (espClient.available()) {
    readByte = espClient.read();
    Serial.write(readByte);
  }
  if (responseCode >= '4'){
    return 0;
  }
  return 1;
}
