import time
import board
#from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
import adafruit_lis3mdl as LIS3MDL
from datetime import datetime
import os
import cv2


def check_value(x_val, y_val):
    return (int(x_val*100) in range(2000, 2600)) and (int(y_val*100) in range(19000,190800))

def take_picture():
    os.system("ffmpeg -i /dev/video2 -frames:v 1 outputX.jpg")
    img = cv2.imread(r'outputX.jpg')



#sensors setup
i2c = board.I2C()
# sensor = LSM6DSOX(i2c)
sensor_2 = LIS3MDL.LIS3MDL(i2c)

#file setup
data_file = open('data.txt', 'a')
now_str = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
data_file.write('\n\n' + now_str + '\n')


while True:
    mag_x, mag_y, mag_z = sensor_2.magnetic
    data_string = 'X:{0:10.2f}, Y:{1:10.2f}'.format(mag_x, mag_y, mag_z)
    if check_value(mag_x, mag_y):
        print("--correct value detected--")
        take_picture()
    print(data_string)
    data_file.write(data_string+'\n')
    time.sleep(0.05)

#when correct values are detected sleep for 0.2 s and then take picure


