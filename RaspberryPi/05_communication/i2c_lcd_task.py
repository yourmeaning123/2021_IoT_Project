from lcd import drivers
import time
import Adafruit_DHT
import datetime

sensor = Adafruit_DHT.DHT11
PIN = 18

display = drivers.Lcd()

try:
    while True:
        now = datetime.datetime.now()
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        if humidity is not None and temperature is not None:
            display.lcd_display_string(now.strftime("%x%X"), 1)
            display.lcd_display_string(f"{temperature:.1f}*C, {humidity:.1f}%", 2)
        else:
            print('Read error')
        time.sleep(1)
finally:
    print("Cleaning Up!")
    display.lcd_clear()