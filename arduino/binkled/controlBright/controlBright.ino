int led = 6;
int brightness = 0;
int fadeAmount = 1;

void setup(){
  pinMode(led,OUTPUT);
}

void loop(){

  analogWrite(led,brightness);

  brightness = brightness + fadeAmount;

  if(brightness <= 0 || brightness >= 80){
    fadeAmount = -fadeAmount;
  }
  

  delay(40);
}
