// By Gary Khodayari
// 2020/10/20

int PIRsensor = 13;
int relay = 8;

void setup() {
  pinMode (PIRsensor, INPUT); //  PIR sensor port is a read port 
  pinMode (relay, OUTPUT); // relay port is a write port
  Serial.begin(9600);
}

void loop() {
  if ( digitalRead(PIRsensor) == 1) { // a loop for if the snesor detects something it wills send a high signal to the port 13
    digitalWrite(relay, HIGH);
    Serial.println("Saw Somthing !!");
  } else { // if nothing is seen the state of the port is chnaged to low
    digitalWrite (relay, LOW);
    Serial.println("no we good for now");
  }
}
