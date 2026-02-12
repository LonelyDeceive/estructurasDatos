int PULSADOR = 2; 
int LED = 7; 
bool buttonState = false;

void setup(){ 

pinMode(PULSADOR, INPUT); 
pinMode(LED, OUTPUT); 
digitalWrite(LED, LOW);

 } 

void loop (){ 

while(digitalRead(PULSADOR) == LOW){ 
 }

if (buttonState == false) {
digitalWrite(LED, HIGH);
buttonState = true;
} else {
digitalWrite(LED, LOW);
buttonState = false;
}
while(digitalRead(PULSADOR) == HIGH){ 
 }
}