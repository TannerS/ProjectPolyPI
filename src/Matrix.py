import threading
import time

class Matrix(threading.Thread):
    w = None
    h = None
    matrix = None

    def __init__(self, data):
        threading.Thread.__init__(self)
        self.matrix = data
        self.h = 8
        self.w = 8
        # self.matrix = [[0 for x in range(self.w)] for y in range(self.h)]

    def run(self):
        json_str = ""

        while True:
            for x in range(self.w):
                print(" ")
                for y in range(self.h):
                  print(self.matrix[x][y], end = " ")
            time.sleep(2)

    def setData(self, data):
        print("update array")
        self.matrix = data