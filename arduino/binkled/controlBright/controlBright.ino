byte listLed[] = {2,3,4,5,6,7,8,9};
byte countLed;

void setup(){
  countLed = sizeof(listLed);
  for(int i = 0; i < countLed; i++){
    pinMode(listLed[i], OUTPUT);
    digitalWrite(listLed[i],LOW);
  }
}

void loop(){

  for(int i = 0;i < countLed; i++){
    digitalWrite(listLed[i], HIGH);
    delay(500);
  }

   for(int i = 0; i < countLed; i++){
    digitalWrite(listLed[i], LOW);
    delay(500);
  }
}
