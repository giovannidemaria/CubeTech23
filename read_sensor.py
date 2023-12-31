import time
import board
# from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
import adafruit_lis3mdl as LIS3MDL
import os

def check_value(x_val, y_val):
    return (int(x_val * 100) in range(2200, 2600)) and (int(y_val * 100) in range(19400, 19600))


def take_pictures(i):
    os.system("ffmpeg -i /dev/video2 -frames:v 1 output" + str(i) + ".jpg")
    # img = cv2.imread(r'output'+i+'.jpg')


# sensors setup
i2c = board.I2C()
# sensor = LSM6DSOX(i2c)
sensor_2 = LIS3MDL.LIS3MDL(i2c)


i = 0
while True:
    mag_x, mag_y, mag_z = sensor_2.magnetic
    if check_value(mag_x, mag_y):
        print("--correct value detected--")
        take_pictures(i)
        i = i + 1
    print(data_string)
    data_file.write(data_string + '\n')
    time.sleep(0.1)

# when correct values are detected sleep for 0.2 s and then take picure
