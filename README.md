# CubeTech23

## For taking a photo:
<code> ffmpeg -f v4l2 -i /dev/video0 -frames:v 1 output4.jpg </code>

## For checking if Intel realsense camera is connected:

<code>lsusb</code>

## in order to start VNC server you need this command:

<codesudo systemctl start vncserver-x11-serviced</code>

An then you wait a little bit. Then you connect using RealVNC client (username and pw are raspi).
