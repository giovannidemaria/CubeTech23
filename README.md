# CubeTech Hackathon

In this repo is provided the code for the CubeTech Hackathon.

It has been hosted by [Leva](https://www.leva.io/) and organized by the [CubeSat Team Polito](https://linktr.ee/cubesatteam). Tasked with developing a system for spacecraft functionality simulation using a Raspberry Pi, I delved deep into Image Recognition and Magnetic Field Analysis.

## For taking a photo (satisfactory enough result):
<code> ffmpeg -i /dev/video2 -frames:v 1 outputX.jpg </code>

## For checking if Intel realsense camera is connected:

<code>lsusb</code>

## in order to start VNC server you need this command:

<code>sudo systemctl start vncserver-x11-serviced</code>

An then you wait a little bit. Then you connect using RealVNC client (username and pw are raspi).

## I am trying to install the Intel SDK for the camera...

this website: <a href="https://github.com/IntelRealSense/librealsense">https://github.com/IntelRealSense/librealsense</a>
