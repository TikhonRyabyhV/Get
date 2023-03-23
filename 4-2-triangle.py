import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
GPIO.setup( dac, GPIO.OUT )

def decimal_2_binary ( value ):
	return [ int (bit) for bit in bin( value )[2:].zfill(8) ]

try:
	while ( True ):
		for i in range( 0, 256 ):
			GPIO.output( dac, decimal_2_binary(i) )
			time.sleep( 4.0 / 255 )

		for i in range( 255, -1, -1 ):
			GPIO.output( dac, decimal_2_binary(i) )
			time.sleep( 4.0 / 255 )
finally:
	GPIO.output( dac, 0 )
	GPIO.cleanup() 
