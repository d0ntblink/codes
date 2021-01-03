//Libraries
#include <DHT.h>
#include <LiquidCrystal.h>

//Constants
#define DHTPIN 2     // what digital pin we're connected to
#define DHTTYPE DHT22   // DHT 22
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);   // tell the RedBoard what pins are connected to the display

//Variables
int chk;
float hum;  //Stores humidity value
float temp; //Stores temperature value

void setup()
{
  lcd.begin(16, 2);
  dht.begin();
  lcd.print("Loading ....");
  delay(1000);
  lcd.clear(); //clear the display
}

void loop()
{
    //Read data and store it to variables hum and temp
    hum = dht.readHumidity();
    temp= dht.readTemperature();
    //Print temp and humidity values to serial monitor
    lcd.setCursor(0, 0);
    lcd.print("Humidity: ");
    lcd.print(hum);
    lcd.print(" %");
    lcd.setCursor(0, 1);
    lcd.print("Temp: ");
    lcd.print(temp);
    lcd.print(" C");
    delay(1000); //Delay 1 sec.
}

   
