import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

GPIO.setup( 14, GPIO.OUT )


for x in 1, 2, 3, 4, 5:
	GPIO.output( 14, 1 )
	time.sleep(2)
	GPIO.output( 14, 0 )
	time.sleep(2)

GPIO.cleanup()


