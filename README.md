# LaserBoy
## Goal
Tried to let roboy highlight objects he could detect with a laser-pointer.

## Achieved:
* Tracking the laser-pointer’s position with image processing
* Controlling and building a mount for the laser-pointer from scratch
* WiFi Communication to the laser-pointer mount
* Model to transform the laser-pointer position to movements of the laser-pointer mount

[Dancing Servos](/presentation_and_assets/ezgif.com-video-to-gif.gif)

## /Arduino_Comm
laser-pointer mount servo control and udp client/server (server: comms.py)

## /Image_Analysis

## /Transformations

## /imageprocessing
viewcamera.py contains a working laser-pointer detection based on HSV values. Also utilizes the highest resolution of the ZED camera.

## /presentation_and_assets
final presentation and some cool LaserBoy assets

## /zed-python
Not tested if the ZED Camera Python wrapper also works for our opencv Laserdetection. Would have been sweet as this would also give us depth values. Just merge-copy-pasted the viewcamera.py into the example/zed_hack.py but run out of time.
