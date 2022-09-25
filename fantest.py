#import the GPIO and time package
import RPi.GPIO as io
import time

io.setmode(io.BCM)
io.setup(18, io.OUT)
while True:
    io.output(18,1)
    time.sleep(1)
    io.output(18,0)
    time.sleep(1)
  
def leds()
