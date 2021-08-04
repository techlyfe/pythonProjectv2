from gpiozero import Button, OutputDevice
from time import sleep

relay1 = OutputDevice(22)
relay2 = OutputDevice(27)
btn = Button(13)
i = 1


def sequence_on():
    global i
    if i == 1:
        print('Lights Sequence running..')
        i = i + 1
    else:
        relay1.on()
        sleep(1)
        relay1.off()
        relay2.on()
        sleep(2)
        relay2.off()


def sequence_off():
    global i
    if i == 2:
        print('Lights Stopped!')
        i = i - 1
    else:
        relay1.off()


print('Hold button to start light Sequence')
print('Press CTRL-C to Exit')

try:
    while True:
        if btn.is_pressed:
            sequence_on()
        else:
            sequence_off()

except KeyboardInterrupt:
    print('  --Program Interrupted')

finally:
    relay1.off()
    relay2.off()
    print('Lights Shutdown, Program Exited')

