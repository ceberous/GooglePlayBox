#!/usr/bin/python

# sudo apt-get install python-dev python-rpi.gpio
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-2

import threading
import time
#import RPi.GPIO as GPIO

#GPIO.setmode( GPIO.BCM )

#GPIO.setup( 23 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
#GPIO.setup( 24 , GPIO.IN , pull_up_down=GPIO.PUD_DOWN )

# you actually don't need to manually "thread-out" the button polling functions. 
# to prove this, actually get this running ont the pi,
# (theoretically) , GPIO.add_event_detect(callback=my_callback) spawns a new thread. (or so were presuming so far)  
# if TRUE, then you can take out the manually thread spawning of the listener helper
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3


def readButtonStateHelperTest():
	print( "Started Waiting around for hardware interrupt" )

	while 1:
		time.sleep(1)
		print( "Simulated - POLL" + str(threading.current_thread()) )
#end readButtonStateHelperTest()

def buttonPressedCallback():

	print( "Callback Func Executed from : "  + str(threading.current_thread()) )

#end buttonPressedCallback()

#GPIO.add_event_detect( 24 , GPIO.RISING , callback=buttonPressedCallback  , bouncetime=200 )

def readButtonStateHelper():

	try:
		#GPIO.wait_for_edge( 23 , GPIO.FALLING )
		print( "Falling Edge Detected" )
		print( str(threading.current_thread()) )
	except KeyboardInterrupt:
		#GPIO.cleanup()
		print("error")

	#GPIO.cleanup()
#end readButtonStateHelper()	

def main():

	t1 = threading.Thread( target=readButtonStateHelperTest , args=() )
	t1.start()

	print( "!!!Main Thread!!!" + str(threading.current_thread()) )

#end main()

main()