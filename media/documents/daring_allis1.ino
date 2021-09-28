
// 6 .Write code turning 3 LED lights using a while loop.

int Red=2;
int Green=3;
int Blue=4;

void setup()
{
  pinMode(Red, OUTPUT);
   pinMode(Green, OUTPUT);
   pinMode(Blue, OUTPUT);
}

void loop()
 
{
   while(r<=5);
  {
  digitalWrite(Red, HIGH);
  delay(1000); 
  digitalWrite(Red, LOW);
    delay(500);
    r++;
  } 
  while(g<=4);
  {
  digitalWrite(Green, HIGH);
  delay(1000); 
  digitalWrite(Green, LOW);
    delay(500);
    g++;
  }
  while(b=2);
  {
  digitalWrite(Blue, HIGH);
  delay(1000); 
  digitalWrite(Blue, LOW);
    delay(500);
    b++;
  }
}