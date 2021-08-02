from gpiozero import LED
from time import sleep

red = LED(22)
amber = LED(27)
green = LED(17)

while True:
    red.on()
    sleep(10)
    red.off()
    amber.on()
    sleep(3)
    amber.off()
    green.on()
    sleep(10)
    green.off()

