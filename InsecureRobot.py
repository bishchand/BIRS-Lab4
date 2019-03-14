from microbit import *
import robotbit

display.show(Image.HAPPY)

while True:

   if (robotbit.sonar(pin1) > 30):
       robotbit.motor(1, 100, 0)
       robotbit.motor(4, -100, 0)
   else:
       robotbit.motorstop(1)
       robotbit.motorstop(4)
       #robotbit.servo(7, 90)
       robotbit.motor(0, 100, 500)
