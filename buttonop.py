#!/usr/bin/python3

from signal import pause
from time import sleep
from gpiozero import LED, Button

lamps_on = False
interval = 0.5

button = Button(13)
led1 = LED(22)
led2 = LED(27)
led3 = LED(17)


def light_seq():
    global lamps_on

    if lamps_on:
        led1.off()
        led2.off()
        led3.off()
    else:

        while not lamps_on:
            led1.on()
            sleep(interval)
            led1.off()
            led2.on()
            sleep(interval)
            led2.off()
            led3.on()
            sleep(interval)
            led3.off()

    lamps_on = not lamps_on


try:
    button.when_pressed = light_seq
    pause()

except KeyboardInterrupt:
    pass

finally:
    led1.close()
    led2.close()
    led3.close()
