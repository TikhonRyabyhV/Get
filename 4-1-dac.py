import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
GPIO.setup( dac, GPIO.OUT ) 

def decimal_2_binary ( value ):
	return [ int (bit) for bit in bin( value )[2:].zfill(8) ]

try:
	while( True ):
		print ( "Please enter integer number from 0 to 255" )
		value = input()

		if( value[0] == 'q' ):
			break
		try:
			value = float(value)
		except ValueError:
			print ( "It is not a number!" ) 
			continue
		int_value = int ( value )
		if( value != float(int_value) ):
			print ( "It is not integer number!" )
			continue
		elif( int_value < 0 or int_value > 255 ):
			print ( "This number is too small or to big." )
			continue
		GPIO.output( dac, decimal_2_binary( int_value ) )
		print( "Expected voltage:" + "{:.4f}".format( 3.3 / 255 * int_value ) + "V" )
		time.sleep( 0.5 )

finally:
	GPIO.output( dac, 0 )
	GPIO.cleanup()
