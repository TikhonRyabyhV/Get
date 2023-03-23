import RPi.GPIO as GPIO
import time
import random


GPIO.setmode( GPIO.BCM )

dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
number = [ ]

for x in range( len( dac ) ):
	number.append( random.randint( 0,1 ) )

print( number )

GPIO.setup( dac, GPIO.OUT )

GPIO.output( dac, number )
time.sleep( 15 )
GPIO.output( dac, 0 )

GPIO.cleanup()
