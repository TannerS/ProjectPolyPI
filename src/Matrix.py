import threading
import time
import RPi.GPIO as GPIO
import time # used for time.sleep()

class Matrix(threading.Thread):
    w = None
    h = None
    matrix = None
    pins = None
    

    def __init__(self, data):
        threading.Thread.__init__(self)
        GPIO.setmode(GPIO.BCM)
        self.matrix = data
        self.h = 8
        self.w = 8
        self.pins = [14,15,18,23,24,25,8,7]
        #self.pins = [4,17,27,6,19,26]
        self.matrix = [[0 for x in range(self.w)] for y in range(self.h)]
        for i in range(len(self.pins)):
            GPIO.setup(self.pins[i], GPIO.OUT)
            print("setting pin: " + str(self.pins[i]))

    def run(self):
        json_str = ""

        while True:
            for x in range(self.w):
                print(" ")
                for y in range(self.h):
                    if (self.matrix[x][y] == 1) and (GPIO.input(self.pins[y]) == False):
                        time.sleep(.15)
                        GPIO.output(self.pins[y], True)


                        #while GPIO.input(self.pins[y]) == True:
                            #print("wait")
                            

                        
                        #time.sleep(.15)
                    elif (self.matrix[x][y] == 0) and (GPIO.input(self.pins[y]) == True):
                        time.sleep(.15)
                        GPIO.output(self.pins[y], False)
                        #while GPIO.input(self.pins[y]) == False:
                            #print("wait")
                    print(self.matrix[x][y], end="")
        

    def setData(self, data):
        print("update array")
        self.matrix = data
