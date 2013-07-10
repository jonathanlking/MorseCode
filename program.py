import time
import string
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.HIGH)

dot = 1
dash = [1,1,1]
space = 0

a = [dot, space, dash] #Dot Dash
b = []

delalTime = 0.1

def letterToMorseCodeBinary(letter):
	print letter
	
def transmitMorseCodeFromList(list):
	for item in list:
		if item is 0:
			GPIO.output(7, GPIO.LOW)
		elif item is 1:
			GPIO.output(7, GPIO.HIGH)
					


listOfCharacters = list("Hello World")
lengthOfList = len(listOfCharacters)

print lengthOfList

for item in listOfCharacters:
        letterToMorseCodeBinary(item)

print "Hello James x ;) The LED Should now come on!"



# The length of a dot is one unit.
# 2. A dash is three units.
# 3. The space between parts of the same letter is one unit.
# 4. The space between letters is three units.
# 5. The space between words is seven units.