import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial
import math

try:
    ser = serial.Serial("COM4", 9600)
except:
    print('no comport connection')

figure1 = plt.figure()

x, y = [], []
angle, distance = [], []


def update1(frame):
    global figure1, x, y, angle, distance
    figure1.cla()
    x = []
    y = []
    angle = []
    distance = []
    for i in range(360):
        cc = str(ser.readline())
        print(cc)
        if cc != '':
            cc = cc[2:][:-5]
            datas = cc.split(", ")
            try:
                distance.append(float(datas[0]))
                angle.append(float(datas[1]))
                distance.append(0)
                angle.append(0)
                x.append(int(math.cos(math.radians(angle))*distance))
                y.append(int(math.sin(math.radians(angle))*distance))
                
            except:
                print("input error")
    #figure1 = plt.scatter(x, y, alpha=0.5)
    figure1 = plt.polar(angle, distance)


animation1 = FuncAnimation(figure1, update1, interval=1000)
#animation2 = FuncAnimation(figure2, update2, interval=1000)
plt.show()
