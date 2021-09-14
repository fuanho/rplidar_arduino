import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial
import numpy as np
import math

try:
    ser = serial.Serial("COM4", 9600)
except:
    print('no comport connection')

figure = plt.figure()

x, y = [], []


def update(frame):
    global figure
    x = []
    y = []
    for i in range(360):
        cc = str(ser.readline())
        if cc != '':
            cc = cc[2:][:-5]
            datas = cc.split(", ")
            try:
                distance = float(datas[0])
                angle = float(datas[1])
                x.append(int(math.cos(math.radians(angle))*distance))
                y.append(int(math.sin(math.radians(angle))*distance))
            except:
                print("input error")
    figure = plt.scatter(x, y, alpha=0.5)


animation = FuncAnimation(figure, update, interval=20)
plt.show()
