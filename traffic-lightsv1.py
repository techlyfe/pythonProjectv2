from gpiozero import LED, Button
from time import sleep
from signal import pause

red = LED(22)
amber = LED(27)
green = LED(17)
on_switch = Button(13)


def light_seq():
    red.on()
    sleep(1)
    red.off()
    amber.on()
    sleep(2)
    amber.off()
    green.on()
    sleep(1)
    green.off()


def stop_seq():
    red.off()
    amber.off()
    green.off()


on_switch.when_pressed = light_seq
on_switch.when_released = stop_seq
pause()
