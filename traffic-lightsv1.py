from gpiozero import LED
from gpiozero import Button
from time import sleep
from signal import pause

red = LED(22)
amber = LED(27)
green = LED(17)
on_switch = Button(13)


def light_seq():
    while True:
        if on_switch.when_pressed:
            red.on()
            sleep(1)
            red.off()
            amber.on()
            sleep(2)
            amber.off()
            green.on()
            sleep(1)
            green.off()
        if on_switch.when_released:
            red.off()
            amber.off()
            green.off()
            break


on_switch.when_pressed = light_seq

pause()
