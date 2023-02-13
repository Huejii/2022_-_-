int buttonPin = 2;
boolean state = LOW;
boolean previousState = LOW;

void setup(){
   pinMode(buttonPin,INPUT);
   Serial.begin(9600);
}
void loop(){
   previousState = state;
   state = digitalRead(buttonPin);

   if(previousState = state;
   state = digitalRead(buttonPin);

   if(previousState == LOW && state == HIGH){
      Serial.println("Push On!");
   }else if(previousState == HIGH && state ==LOW){
      Serial.println("Push Off!");
   }
   delay(20);
}