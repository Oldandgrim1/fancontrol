#import the GPIO and time package
import RPi.GPIO as io
from time import asctime, sleep
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8') ##forces utf-8 encoding.

#Set up GPIO pins
io.setmode(io.BCM)
io.setup(17, io.OUT) #gpio17
io.setup(27, io.OUT) #gpio27
io.setup(22, io.OUT) #gpio22
#This code reused from https://github.com/Oldandgrim1/Raspberry-Pi-SenseHat-Monitor-Project

pi1 = subprocess.run(['/home/pi/code/fancontrol/pi4temp.sh'],universal_newlines= True, capture_output= True) 
pi2 = subprocess.run(['/home/pi/code/fancontrol/pi1temp.sh'],universal_newlines= True, capture_output= True)
pi3 = subprocess.run(['/home/pi/code/fancontrol/pi2temp.sh'],universal_newlines= True, capture_output= True)
pi4 = subprocess.run(['/home/pi/code/fancontrol/pi3temp.sh'],universal_newlines= True, capture_output= True)
pi1int = int(pi1.stdout)
pi2int = int(pi2.stdout)
pi3int = int(pi3.stdout)
pi4int = int(pi4.stdout) 
#print temps for debugging
print (pi1int)
print (pi2int)
print (pi3int)
print (pi4int)
avg = (pi1int + pi2int + pi3int + pi4int)/4
topavg = int(pi1int + pi2int)/2
botavg = int(pi3int + pi4int)/2

avgint = int(avg)
print (avg)
print (avgint)
print (topavg)
print (botavg)
#def fan1():
#    if (avgint > 60):
         

