from gpiozero import LED, Button
from timr import sleep
led = LED(17)
button = Button(2)

while True:
   buttton.wait_for_press()
   led.toggle()
   sleep(0.5)

