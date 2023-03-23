import RPi.GPIO as GPIO
import time
import random


GPIO.setmode( GPIO.BCM )

dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
number = [ [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [ 1, 1, 1, 1, 1, 1, 1, 1] ]

print( number )

GPIO.setup( dac, GPIO.OUT )

for i in range( len( number ) ):
	GPIO.output( dac, number[i] )
	time.sleep( 15 )

GPIO.output( dac, 0 )

GPIO.cleanup()

