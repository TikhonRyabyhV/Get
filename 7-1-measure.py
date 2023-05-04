import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plot

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

exp_data = []
volt_k = 3.3 / ( 2**8 )

try:
	start_time = time.time()
	GPIO.output( troyka, 1 )
	while( True ):
		time.sleep( 0.008 )
		value = adc( dac, comp )
		print( "Number  " + str(value) + ", expected voltage:" + "{:.4f}".format( value * volt_k ) + "V" )
		exp_data.append(value)

		volume = [0] * 8
		for i in range( int( value / 255 * 8 ) ):
			volume[i] = 1
		GPIO.output( leds, volume )
		time.sleep( 0.1 )

		if( (value * volt_k) >= 2.7 ):
			break

	GPIO.output( troyka, 0  )
	while( True ):
		time.sleep( 0.008 )
		value = adc( dac, comp )
		print( "Number  " + str(value) + ", expected voltage:" + "{:.4f}".format( value * volt_k ) + "V" )
		exp_data.append(value)

		volume = [0] * 8
		for i in range( int( value / 255 * 8 ) ):
			volume[i] = 1
		GPIO.output( leds, volume )
		time.sleep( 0.1 )

		if( (value * volt_k) <= 0.07 ):
			break
finally:
	GPIO.output( troyka, 0 )
	all_time = time.time() - start_time

	with open( "data.txt", "w" ) as output_file:
		for x in exp_data:
			output_file.write( str(x) + "\n" )

	with open( "settings.txt", "w" ) as output_file_2:
		output_file_2.write( "Descrertiztion freq.:  " +"{:.4f}".format(  len( exp_data ) / all_time ) + " Hz" + "\nQuant. step:  " + "{:.4f}".format( volt_k  ) + " V" )

	plot.plot (exp_data)
	plot.show()

	GPIO.output( dac, 0 )
	GPIO.output( troyka, 0 )
	GPIO.output( leds, 0 )
	GPIO.cleanup()

