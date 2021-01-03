#include <LiquidCrystal.h>



//Constants
int red = 4;                      //red led pin
int green = 3;                    // green led pin
int buzzer = 2;                   //busser pin
int smokeA0 = A2;                 // analog port for smoke
int threshhold = 150;             //monoxide level threshold
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);   // tell the RedBoard what pins are connected to the display



void setup() {
  // put your setup code here, to run once:
  pinMode(red, OUTPUT);                   // all the pins for outputting votage
  pinMode(green, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(smokeA0, INPUT);                // reading analog port
  lcd.begin(16, 2);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int analogSensor = analogRead(smokeA0);
  Serial.print("Pin A0: ");
  Serial.println(analogSensor);
  lcd.setCursor(0, 0);
  lcd.print(analogSensor);
  if (analogSensor > threshhold) {                     // if monoxide level is fine
    digitalWrite(red, HIGH);                            // turn red led on green led off
    digitalWrite(green, LOW);
    tone(buzzer, 1000, 200);
    lcd.setCursor(0, 1);
    lcd.print("LMAO RIP");
  }
  else {                                              // if its bad
    digitalWrite(red, LOW);
    digitalWrite(green, HIGH);
    noTone(buzzer);
    lcd.setCursor(0, 1);
    lcd.print("WE GUCCI");
  }
  delay(1000);
}
