int incomingByte;
void setup() {
  Serial.begin(9600);
  pinMode (13, OUTPUT);
  pinMode (12, OUTPUT);
  // put your setup code here, to run once:
}

void loop() {
  // R turns the red led on and yellow led off, Y turns the yellow led on and red led off:
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'R') {
      digitalWrite (13, HIGH);
      digitalWrite (12, LOW);
    }
    if (incomingByte == 'Y') {
      digitalWrite (12, HIGH);
      digitalWrite (13, LOW);
    }
  }
}
