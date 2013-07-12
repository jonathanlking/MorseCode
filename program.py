import time
import string
import RPi.GPIO as GPIO

delayTime = 0.1
string = "Hello World"

dot = [1]
dash = [1,1,1]
space = [0]


# The length of a dot is one unit.
# 2. A dash is three units.
# 3. The space between parts of the same letter is one unit.
# 4. The space between letters is three units.
# 5. The space between words is seven units.

a = dot + space + dash #Dot Dash
b = dash + space + dot + space + dot + space + dot
c = dash + space + dot + space + dash + space + dot
d = dash + space + dot + space + dot
e = dot
f = dot + space + dot + space + dash + space + dot
g = dash + space + dash + space + dot 
h = dot + space + dot + space + dot + space + dot
i = dot + space + dot
j = dot + space + dash + space + dash + space + dash
k = dash + space + dot + space + dash
l = dot + space + dash + space + dot + space + dot 
m = dash + space + dash 
n = dash + space + dot 
o = dash + space + dash + space + dash 
p = dot + space + dash + space + dash + space + dot 
q = dash + space + dash + space + dot + space + dash
r = dot + space + dash + space + dot
s = dot + space + dot + space + dot 
t = dash
u = dot + space + dot + space + dash
v = dot + space + dot + space + dot + space + dash
w = dot + space + dash + space + dash
x = dash + space + dot + space + dot + space + dash
y = dash + space + dot + space + dash + space + dash
z = dash + space + dash + space + dot + space + dot


def characterToMorseCodeBinary(letter):
	if letter is 'a': return a
	elif letter is 'b': return b
	elif letter is 'c': return c
	elif letter is 'd': return d
	elif letter is 'e': return e
	elif letter is 'f': return f
	elif letter is 'g': return g
	elif letter is 'h': return h
	elif letter is 'i': return i
	elif letter is 'j': return j
	elif letter is 'k': return k
	elif letter is 'l': return l
	elif letter is 'm': return m
	elif letter is 'n': return n
	elif letter is 'o': return o
	elif letter is 'p': return p
	elif letter is 'q': return q
	elif letter is 'r': return r
	elif letter is 's': return s
	elif letter is 't': return t
	elif letter is 'u': return u
	elif letter is 'v': return v
	elif letter is 'w': return w
	elif letter is 'x': return x
	elif letter is 'y': return y
	elif letter is 'z': return z


	
def transmitMorseCodeFromList(list):

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
					


listOfCharacters = list(string.lower())

binaryArray = [0,0]

for item in listOfCharacters:
	print characterToMorseCodeBinary(item)
        # binaryArray.extend(characterToMorseCodeBinary(item))
        
transmitMorseCodeFromList([1,0,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,0,1,0,1])




