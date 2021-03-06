from lcd import drivers
import time

display = drivers.Lcd()

try:
    print("Waiting to display")
    display.lcd_display_string("Hello, World!", 1)
    
    while True:
        display.lcd_display_string("** WELCOME **", 2)
        time.sleep(2)
        display.lcd_display_string("WELCOME", 2)
        time.sleep(2)
finally:
    print("Cleaning Up!")
    display.lcd_clear()