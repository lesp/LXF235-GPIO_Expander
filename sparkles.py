from gpiozero import LED, Button
from time import sleep
from random import uniform
from signal import pause
red = LED(17)
blue = LED(27)
green = LED(22)
button = Button(10)
def sparkles():
    x = uniform(0.1, 3.0)
    print(x)
    for i in range(3):
        red.on()
        sleep(x)
        red.off()
        sleep(x)
        blue.on()
        sleep(x)
        blue.off()
        sleep(x)
        green.on()
        sleep(x)
        green.off()
        sleep(x)

button.when_pressed = sparkles
pause()
