import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

leds = [ 21, 20, 16, 12, 7, 8, 25, 24 ]
GPIO.setup( leds, GPIO.OUT )

for i in range( 3 ):
    for x in leds:
        GPIO.output( x, 1 )
        time.sleep( 0.5 )
        GPIO.output( x, 0 )

GPIO.output( leds, 0 )
GPIO.cleanup()
