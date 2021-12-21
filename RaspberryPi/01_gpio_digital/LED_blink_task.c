#include <wiringPi.h>
#define LED_PIN1 4
#define LED_PIN2 5
#define LED_PIN3 6
int main (void)
{
  wiringPiSetupGpio() ;
  pinMode (LED_PIN1, OUTPUT) ;
  pinMode (LED_PIN2, OUTPUT) ;
  pinMode (LED_PIN3, OUTPUT) ;

digitalWrite (LED_PIN1, HIGH) ; delay (2000) ;
digitalWrite (LED_PIN1,  LOW) ;
digitalWrite (LED_PIN2, HIGH) ; delay (2000) ;
digitalWrite (LED_PIN2,  LOW) ;
digitalWrite (LED_PIN3, HIGH) ; delay (2000) ;
digitalWrite (LED_PIN3,  LOW) ;
  

}