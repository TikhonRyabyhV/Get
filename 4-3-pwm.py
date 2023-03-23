import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
GPIO.setup( dac, GPIO.OUT )

def decimal_2_binary ( value ):
	return [ int (bit) for bit in bin( value )[2:].zfill(8) ]

GPIO.setup( 24, GPIO.OUT )
GPIO.setup( 18, GPIO.OUT )

pin1 = GPIO.PWM( 24, 100 )
pin2 = GPIO.PWM( 18, 100 )
pin1.start(0)
pin2.start(0)

try:
	while( True ):
		duty_cycle = float ( input( "Please enter duty cycle in percent:" ) )
		pin1.start( min( 100, duty_cycle ) )
		pin2.start( min( 100, duty_cycle ) )
		print( "Expected voltage:" + "{:.4f}".format( 3.3 * min( 100, duty_cycle ) / 100 ) + "V" )
		GPIO.output( dac, decimal_2_binary(  int ( min( 100, int (duty_cycle) ) * 255 / 100 ) ) )

finally:
	GPIO.output( dac, 0 )
	GPIO.cleanup()
