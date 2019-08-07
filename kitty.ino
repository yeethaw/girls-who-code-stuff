#include <Servo.h>                           // Include servo library

int left_whisker = 5;
int right_whisker = 7;

int piezo = A2;

int sensor_reading = 0;
int threshold = 5;

Servo servoRight;
Servo servoLeft;


void forwards(int delayy){
  servoLeft.writeMicroseconds(1700);        
  servoRight.writeMicroseconds(1300);
  delay(delayy);
}

void backwards(int delayy){
  servoLeft.writeMicroseconds(1300);        
  servoRight.writeMicroseconds(1700);
  delay(delayy);
}

void spin_left(int delayy){
  servoLeft.writeMicroseconds(1300);        
  servoRight.writeMicroseconds(1300);
  delay(delayy);
}

void spin_right(int delayy){
  servoLeft.writeMicroseconds(1700);        
  servoRight.writeMicroseconds(1700);
  delay(delayy);
}

void moveKitty() {
  // Your Code Here
}

void stopKitty(int delayy) {
  // Your Code Here
  servoLeft.writeMicroseconds(1500);        
  servoRight.writeMicroseconds(1500);
  delay(delayy);
}

void setup() {
  servoLeft.attach(13);                      
  servoRight.attach(12); 

  pinMode(left_whisker , INPUT);
  pinMode(right_whisker, INPUT);
  pinMode(piezo , INPUT);
  
  Serial.begin(9600);          //use the serial port
  Serial.println("setup completed!");
 
}

void loop(){
  // put your main code here, to run repeatedly:
  sensor_reading = analogRead(piezo);

  int left_whisker_value = digitalRead(left_whisker);
  int right_whisker_value = digitalRead(right_whisker); 

  if (sensor_reading >= threshold){
    Serial.println("STOP");
    stopKitty(5000);
  }

  if (left_whisker_value == 1 && right_whisker_value == 1){
    Serial.println("ONWARDS TO BERLIN!!");
    forwards(500);
  }

  if (left_whisker_value == 0 && right_whisker_value == 0) {
    Serial.println("RETREAT");
    backwards(4000);
    spin_right(500);
  }

  if (left_whisker_value == 0 && right_whisker_value == 1){
    Serial.println("SPINNING RIGHT");   
    spin_right(500);
  }
  if (left_whisker_value == 1 && right_whisker_value == 0){
    Serial.println("SPINNING LEFT");   
    spin_left(500);
  }
}
