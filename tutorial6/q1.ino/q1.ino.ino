#include <stdint.h>

void setup() {
  uint8_t DDRD, DDRB, PINB, PORTD;
  DDRD = DDRD | 0x01;
  DDRB = DDRB | 0x00;
  int8_t count = 10;
  uint8_t tmp = 0;
  
  while(true) {
    tmp = PINB & 0x01;
    if(tmp == 0x01) {
      PORTD |= 0x01;
    }
    else PORTD &= 0x00;
  }
}
