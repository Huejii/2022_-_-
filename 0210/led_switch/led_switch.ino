int buttonPin = 11;
int ledPin = 13;

void setup()
{
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
  
}

void loop()
{
  int buttonState = digitalRead(buttonPin);
  
  if(buttonState == HIGH) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
   
  delay(10);
  
}