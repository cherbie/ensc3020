#include <stdint.h>

void setup() {
  // put your setup code here, to run once:
  int8_t DDRD, PORTD;
  DDRD = DDRD | 0b00000001; //PD0 set as output
  while(true) {
    PORTD = PORTD | 0x01;
    delay(1000);
    PORTD = PORTD & 0xFE;
    delay(1000);
  }
}

void loop() {
  // put your main code here, to run repeatedly:

}
