from gpiozero import LED
from gpiozero import Button
from time import sleep

red = LED(22)
amber = LED(27)
green = LED(17)
on_switch = Button(13)


while True:
    if button.is_pressed:
        red.on()
        sleep(1)
        red.off()
        amber.on()
        sleep(2)
        amber.off()
        green.on()
        sleep(1)
        green.off()
    else:
        print("Waiting on Button to be pressed")
