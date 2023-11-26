import time
import board
#from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
import adafruit_lis3mdl as LIS3MDL
from datetime import datetime

#sensors setup
i2c = board.I2C()
# sensor = LSM6DSOX(i2c)
sensor_2 = LIS3MDL.LIS3MDL(i2c)

#file setup
data_file = open('data.txt', 'a')
now_str = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
data_file.write('\n\n' + now_str + '\n')

scan = True

while scan:
    mag_x, mag_y, mag_z = sensor_2.magnetic
    data_string = 'X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT'.format(mag_x, mag_y, mag_z)
    if check_value(mag_x, mag_y, mag_z):
        print("--correct value detected--")
        #scan = False
    print(data_string)
    data_file.write(data_string+'\n')
    time.sleep(0.5)



def check_value(x_val, y_val, z_val):
    if x_val*100 in range(2871, 2934) and y_val in range() and  z_val in range():