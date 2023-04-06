import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
GPIO.setup( dac, GPIO.OUT )

comp = 4
troyka = 17
GPIO.setup( comp, GPIO.IN )
GPIO.setup( troyka, GPIO.OUT, initial = 0 )

leds = [ 24, 25, 8, 7, 12, 16, 20, 21 ]
GPIO.setup( leds, GPIO.OUT )

def decimal_2_binary ( value ):
	return [ int (bit) for bit in bin( value )[2:].zfill(8) ]

def adc ( dac, comp ):
	result = 0
	for i in range( 8 ):
		result += 2**( 7 - i )
		GPIO.output( dac, decimal_2_binary( result ) )
		time.sleep(0.008)
		if( GPIO.input( comp ) == 0 ):
			result -= 2**( 7 - i )
	GPIO.output( dac, 0 )
	return result;
try:
	while( True ):
		time.sleep(0.008)
		number = adc( dac, comp )
		voltage = number / 256 * 3.3
		print( "Number  " + str(number) + ", expected voltage:" + "{:.4f}".format( voltage ) + "V" )
		volume = [0] * 8
		for i in range( int( number / 255 * 8 ) ):
			volume[i] = 1
		GPIO.output( leds, volume )
		time.sleep( 0.5 )

finally:
	GPIO.output( dac, 0 )
	GPIO.output( troyka, 0 )
	GPIO.output( leds, 0 )
	GPIO.cleanup()

