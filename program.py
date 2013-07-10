import time
import string
import RPi.GPIO as GPIO

dot = 1
dash = [1,1,1]
space = 0

a = [dot, space, list(dash)] #Dot Dash
b = []



delayTime = 1



def letterToMorseCodeBinary(letter):
	print letter
	
def transmitMorseCodeFromList(list):

# 	print list
# 	

# 	
# 	GPIO.output(7, GPIO.HIGH)
# 	time.sleep(delayTime)
# 	GPIO.output(7, GPIO.LOW)
# 	time.sleep(delayTime)
# 	GPIO.output(7, GPIO.HIGH)
# 	time.sleep(delayTime)
	
	for item in list:
		if item is 0:
			GPIO.cleanup()
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(7, GPIO.OUT)
			GPIO.output(7, GPIO.LOW)
			time.sleep(delayTime)
			GPIO.cleanup()
		elif item is 1:
			GPIO.cleanup()
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(7, GPIO.OUT)
			GPIO.output(7, GPIO.HIGH)
			time.sleep(delayTime)
			GPIO.cleanup()
					


listOfCharacters = list("Hello World")
lengthOfList = len(listOfCharacters)

# print lengthOfList
testCodeList = [1,0,0,1,1,1,0,0,1]
transmitMorseCodeFromList(a)

for item in listOfCharacters:
        letterToMorseCodeBinary(item)



# The length of a dot is one unit.
# 2. A dash is three units.
# 3. The space between parts of the same letter is one unit.
# 4. The space between letters is three units.
# 5. The space between words is seven units.