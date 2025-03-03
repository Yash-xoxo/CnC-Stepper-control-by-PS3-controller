const int stepX = 2;
const int dirX  = 5;
const int stepY = 3;
const int dirY  = 6;
const int enPin = 8;

bool moveX = false, moveY = false;
int dirXState = HIGH, dirYState = HIGH;

void setup() {
  pinMode(stepX, OUTPUT);
  pinMode(dirX, OUTPUT);
  pinMode(stepY, OUTPUT);
  pinMode(dirY, OUTPUT);
  pinMode(enPin, OUTPUT);

  digitalWrite(enPin, LOW);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();

    switch (command) {
      case 'X': moveX = true; dirXState = HIGH; break; // Move X forward
      case 'x': moveX = true; dirXState = LOW; break;  // Move X backward
      case 'S': moveX = false; moveY = false; break;   // Stop all motors
      case 'Y': moveY = true; dirYState = HIGH; break; // Move Y forward
      case 'y': moveY = true; dirYState = LOW; break;  // Move Y backward
    }

    digitalWrite(dirX, dirXState);
    digitalWrite(dirY, dirYState);
  }

  // Slowest speed: Increase delay between steps
  if (moveX) {
    digitalWrite(stepX, HIGH);
    delay(10);  // 5 milliseconds per step (adjust for slower speed)
    digitalWrite(stepX, LOW);
    delay(10);
  }

  if (moveY) {
    digitalWrite(stepY, HIGH);
    delay(10);  // 5 milliseconds per step (adjust for slower speed)
    digitalWrite(stepY, LOW);
    delay(10);
  }
}



