#!/usr/bin/python3

from signal import pause
from time import sleep
from gpiozero import LED, Button

blink_on = False
interval = 0.5

button = Button(21)
led1 = LED(26)
led2 = LED(19)


def go_blink():
    global blink_on

    if blink_on:
        led1.off()
        led2.off()
    else:
        led1.blink(interval, interval)
        sleep(interval)
        led2.blink(interval, interval)

    blink_on = not blink_on


try:
    button.when_pressed = go_blink
    pause()

except KeyboardInterrupt:
    pass

finally:
    led1.close()
    led2.close()