
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#define crossLine 20
// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
// you can also call it with a different address you want
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);

int firstColor[] = {1024, 0, 2560};//blue
int secondColor[] = {2560, 512, 0};//orange


//int firstColor[] = {0, 1152, 3840};//blue
//int secondColor[] = {2560, 512, 0};//orange
//int thirdColor[] = {1024, 0, 2560};//zerg
//int forthColor[] = {0, 0, 512};//terran
void setup() {
  Serial.begin(9600);
  Serial.println("16 channel PWM test!");

  pwm.begin();
  pwm.setPWMFreq(1000);
  for (int i = 0; i < 16; i++) {
    pwm.setPWM(i, 0, 0);
  }
  delay(2000);
  for (int i = 0; i < crossLine; i++) {
    pwm.setPWM(0, 0, ((4096 / 100) *i) );
    pwm.setPWM(1, 0, ((4096 / 100) * i) );
    pwm.setPWM(2, 0, ((4096 / 100) * i) );
    delay(20);
  }
}

void loop() {

  protosAlert(firstColor[0], firstColor[1], firstColor[2], 100, 4);
  protosAlert(firstColor[0], firstColor[1], firstColor[2], 100, 3);
  protosAlert(firstColor[0], firstColor[1], firstColor[2], 100, 2);
  protosAlert(firstColor[0], firstColor[1], firstColor[2], 100, 1);
  protosAlertLogo(4096, 4096, 4096, 100, 0);
  fadeOut(firstColor[0], firstColor[1], firstColor[2], 1);
  fadeOut(firstColor[0], firstColor[1], firstColor[2], 2);
  fadeOut(firstColor[0], firstColor[1], firstColor[2], 3);
  fadeOut(firstColor[0], firstColor[1], firstColor[2], 4);
  delay(2000);
  
  protosAlert(secondColor[0], secondColor[1], secondColor[2], 100, 4);
  protosAlert(secondColor[0], secondColor[1], secondColor[2], 100, 3);
  protosAlert(secondColor[0], secondColor[1], secondColor[2], 100, 2);
  protosAlert(secondColor[0], secondColor[1], secondColor[2], 100, 1);
  protosAlertLogo(4096, 4096, 4096, 100, 0);
  fadeOut(secondColor[0], secondColor[1], secondColor[2], 1);
  fadeOut(secondColor[0], secondColor[1], secondColor[2], 2);
  fadeOut(secondColor[0], secondColor[1], secondColor[2], 3);
  fadeOut(secondColor[0], secondColor[1], secondColor[2], 4);

  delay(2000);
}

void protosAlert(int r, int g, int b, int value, int pixel) {
  for (int i = crossLine; i <= value ; i++) {
    pwm.setPWM(pixel * 3, 0, ((r / 100) *i) );
    pwm.setPWM(pixel * 3 + 1, 0, ((g / 100) * i) );
    pwm.setPWM(pixel * 3 + 2, 0, ((b / 100) * i) );
    delayMicroseconds(100);
  }
  for (int i = value; i > crossLine; i--) {
    pwm.setPWM(pixel * 3, 0, ((r / 100) *i) );
    pwm.setPWM(pixel * 3 + 1, 0, ((g / 100) * i) );
    pwm.setPWM(pixel * 3 + 2, 0, ((b / 100) * i) );
    delayMicroseconds(300);
  }
}

void protosAlertLogo(int r, int g, int b, int value, int pixel) {
  for (int i = crossLine; i <= value ; i++) {
    pwm.setPWM(pixel * 3, 0, ((r / 100) *i) );
    pwm.setPWM(pixel * 3 + 1, 0, ((g / 100) * i) );
    pwm.setPWM(pixel * 3 + 2, 0, ((b / 100) * i) );
    delayMicroseconds(200);
  }
  //delay(500);
  for (int i = value; i > crossLine; i--) {
    pwm.setPWM(pixel * 3, 0, ((r / 100) *i) );
    pwm.setPWM(pixel * 3 + 1, 0, ((g / 100) * i) );
    pwm.setPWM(pixel * 3 + 2, 0, ((b / 100) * i) );
    delayMicroseconds(600);
  }
}

void fadeOut(int r, int g, int b, int pixel) {
  for (int i = crossLine; i >= 0; i--) {
    pwm.setPWM(pixel * 3, 0, ((r / 100) *i) );
    pwm.setPWM(pixel * 3 + 1, 0, ((g / 100) * i) );
    pwm.setPWM(pixel * 3 + 2, 0, ((b / 100) * i) );
    delay(10);
  }
}