import RPi.GPIO as GPIO
import time 

LED_PIN = 4
switch_pin = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항

try:
    while True:
        val = GPIO.input(switch_pin) #누르지 않은 경우 0, 눌렀을 때는 1
        print(val)
        time.sleep(0.1)
        GPIO.output(LED_PIN, val) #GPIO.HIGH (1), GPIO.LOW (0)
finally:
    GPIO.cleanup()
    print("cleanup and exit")