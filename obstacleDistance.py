# This function is used to calculate the obstacle distance from the bot

def calc(TRIG,ECHO):
    # setup the pinModes for the trigger and echo pins of Ultrasonic Sensor
	GPIO.setup(TRIG,GPIO.OUT)       
	GPIO.setup(ECHO,GPIO.IN)

	# Then, ensure that the Trigger pin is set low, and give the sensor a second to settle.
	GPIO.output(TRIG, False)
	print("Waiting For Sensor To Settle")
	time.sleep(2)

    # Send a pulse from the Ultrasonic Sensor
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
    
    # Note the sending time and recieving time of the pulse
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

    # Calculate obstacle distance
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration x 17150
	distance = round(distance, 2)
    return distance
    GPIO.cleanup()
