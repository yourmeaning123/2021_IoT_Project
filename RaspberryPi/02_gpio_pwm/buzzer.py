import RPi.GPIO as GPIO
import time 

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [262, 294, 330, 349, 392, 440, 494, 523]
FL = [392, 392, 440, 440, 392, 392, 330, 330, 392, 392, 330, 330 , 294, 294, 294]
SL = [392, 392, 440, 440, 392, 392, 330, 330, 392, 330, 294, 330 , 262, 262, 262]
try:
    for i in FL :
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    for i in SL :
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
finally:
    pwm.stop()
    GPIO.cleanup()