# CubeTech23

## For taking a photo (Unsatisfactory result):
<code> ffmpeg -f v4l2 -i /dev/video0 -frames:v 1 output4.jpg </code>

## For checking if Intel realsense camera is connected:

<code>lsusb</code>

## in order to start VNC server you need this command:

<code>sudo systemctl start vncserver-x11-serviced</code>

An then you wait a little bit. Then you connect using RealVNC client (username and pw are raspi).

## I am trying to install the Intel SDK for the camera...

this website: <a href="https://github.com/IntelRealSense/librealsense">https://github.com/IntelRealSense/librealsense</a>
