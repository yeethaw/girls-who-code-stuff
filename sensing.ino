int left_whisker = 5;
int right_whisker = 7;

int piezo = A2;

int sensor_reading = 0;
int threshold = 5;

void setup() {
  // put your setup code here, to run once:

  pinMode(left_whisker , INPUT);
  pinMode(right_whisker, INPUT);
  pinMode(piezo , INPUT);
  
  Serial.begin(9600);          //use the serial port
  Serial.println("setup completed!");
}

void loop() {
  // put your main code here, to run repeatedly:

  sensor_reading = analogRead(piezo);
  Serial.println(sensor_reading);

  if (sensor_reading >= threshold){
    Serial.println("KNOCK!");
    delay(500);
  }

  int left_whisker_value = digitalRead(left_whisker);
  int right_whisker_value = digitalRead(right_whisker);

  if (left_whisker_value == 0 && right_whisker_value == 0){
    Serial.println("both whiskers pressed");
  }
  else if (left_whisker_value == 0 && right_whisker_value == 1){
    Serial.println("left whisker pressed");
  }
  else if (left_whisker_value == 1 && right_whisker_value == 0){
    Serial.println("right whisker pressed");
  }

  else{
    Serial.println("no whiskers pressed");
  }
  
  delay(500); // delay to avoid overloading the serial port buffer
}
