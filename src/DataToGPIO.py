#pyPractice
import RPi.GPIO as GPIO
import time # used for time.sleep()

GPIO.setmode(GPIO.BCM)

pin_IN = 27
pin_OUT = 5

GPIO.setup(pin_IN, GPIO.IN)
GPIO.setup(pin_OUT, GPIO.OUT)

# initializes the array. The following code initializes the contents of the
# array to 0. However, the array from Java will not be a proper array initially. Deserialize it before setting it equal to this one.

w, h = 8, 8; # change these values if you decide that less buttons should be clicked. For example, if you decide on a 4x4 grid of buttons, change 8, 8 to 4, 4.

Matrix = [[0 for x in range(w)] for y in range(h)]

try:
    while True:
        for x in range(len(Matrix)):
            for y in range(len(Matrix)):
                print(x)
            # if matrix[y][x] is true (access by columns, not rows. Since the first index is used by rows usually, this syntax should be right.)
                # GPIO.output(pinOut) = true
        # delay the playing of notes for some amount of time. use time.sleep(sec), where sec is an integer or float.
        time.sleep(1)
        # update the matrix by getting new input from android app. 
finally:
    GPIO.cleanup()
