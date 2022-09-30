#import the GPIO and time package
import RPi.GPIO as io
import time
#Test LED and pin status.
io.setmode(io.BCM)
io.setup(17, io.OUT) #gpio17
io.setup(27, io.OUT) #gpio27
io.setup(22, io.OUT) #gpio22

while True:
    time.sleep(1)
    io.output(17,0)
    time.sleep(0.25)
    io.output(17,1)
    time.sleep(0.25)
    io.output(27,1)
    time.sleep(0.25)
    io.output(27,0)
    time.sleep(0.25)
    io.output(22,1)
    time.sleep(0.25)
    io.output(22,0)
    

#Test concluded, GPIO pins work and I know how to light them and which order to use, now to write the if/else/then conditionals in the next bit of code.


#GPIO pin guide, taken from the pinout command.
#J8:
#   3V3  (1) (2)  5V    
# GPIO2  (3) (4)  5V    
# GPIO3  (5) (6)  GND   
# GPIO4  (7) (8)  GPIO14
#   GND  (9) (10) GPIO15
#GPIO17 (11) (12) GPIO18
#GPIO27 (13) (14) GND   
#GPIO22 (15) (16) GPIO23
#   3V3 (17) (18) GPIO24
#GPIO10 (19) (20) GND   
# GPIO9 (21) (22) GPIO25
#GPIO11 (23) (24) GPIO8 
#   GND (25) (26) GPIO7 
# GPIO0 (27) (28) GPIO1 
# GPIO5 (29) (30) GND   
# GPIO6 (31) (32) GPIO12
#GPIO13 (33) (34) GND   
#GPIO19 (35) (36) GPIO16
#GPIO26 (37) (38) GPIO20
#   GND (39) (40) GPIO21  

