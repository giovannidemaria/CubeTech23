# CubeTech23

## For taking a photo (satisfactory enough result):
<code> ffmpeg -i /dev/video2 -frames:v 1 outputX.jpg </code>

## For checking if Intel realsense camera is connected:

<code>lsusb</code>

## in order to start VNC server you need this command:

<code>sudo systemctl start vncserver-x11-serviced</code>

An then you wait a little bit. Then you connect using RealVNC client (username and pw are raspi).

## I am trying to install the Intel SDK for the camera...

this website: <a href="https://github.com/IntelRealSense/librealsense">https://github.com/IntelRealSense/librealsense</a>
