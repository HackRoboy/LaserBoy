########################################################################
#
# Copyright (c) 2017, STEREOLABS.
#
# All rights reserved.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
########################################################################

"""
    Live camera sample showing the camera information and video in real time and allows to control the different
    settings.
"""

import cv2
import pyzed.camera as zcam
import pyzed.types as tp
import pyzed.core as core
import pyzed.defines as sl

camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_BRIGHTNESS
str_camera_settings = "BRIGHTNESS"
step_camera_settings = 1

import cv2
import numpy as np
vs = cv2.VideoCapture(0)
if not(vs.isOpened()):
    vs.open()

if hasattr(cv2, 'cv'):
    vs.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 4416)
    vs.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1242)
else:
    vs.set(cv2.CAP_PROP_FRAME_WIDTH, 4416)
    vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 1242)
while True:
    ok, frame = vs.read()
    frame = frame[0:1242, 0:2208]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #chipbag settings
    #lower = np.array([0, 200, 200])
    #upper = np.array([5, 255, 255])
    #lower2 = np.array([170, 200, 200])
    #upper2 = np.array([180, 255, 255])

    lower = np.array([0, 70, 200])
    upper = np.array([5, 180, 255])
    lower2 = np.array([170, 70, 200])
    upper2 = np.array([180, 180, 255])

    mask = cv2.inRange(hsv, lower, upper)
    mask2 = cv2.inRange(hsv, lower2, upper2)

    maskc = cv2.add(mask, mask2)

    res = cv2.bitwise_and(frame, frame, mask=maskc)

    im2, contours, hierarchy = cv2.findContours(maskc, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
    if contours:
        # compute the center of the contour
        M = cv2.moments(contours[0])
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # draw the contour and center of the shape on the image
            # cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
            # cv2.circle(frame, (cX, cY), 7, (0, 255, 0), -1)
            # cv2.putText(frame, "center", (cX - 20, cY - 20),
            #			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.drawMarker(frame, (cX, cY), (0, 255, 0), markerSize=200, thickness=20)
    else:
        print("Nothing found")
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 600,600)
    cv2.namedWindow('maskc', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('maskc', 600, 600)
    cv2.moveWindow('maskc',600,0)
    cv2.imshow("frame", frame)
    cv2.imshow("maskc", maskc)
    cv2.waitKey(2)
cv2.destroyAllWindows()


def main():
    print("Running...")
    init = zcam.PyInitParameters()
    cam = zcam.PyZEDCamera()
    if not cam.is_opened():
        print("Opening ZED Camera...")
    status = cam.open(init)
    if status != tp.PyERROR_CODE.PySUCCESS:
        print(repr(status))
        exit()

    runtime = zcam.PyRuntimeParameters()
    mat = core.PyMat()

    print_camera_information(cam)
    print_help()

    key = ''
    while key != 113:  # for 'q' key
        err = cam.grab(runtime)
        if err == tp.PyERROR_CODE.PySUCCESS:
            cam.retrieve_image(mat, sl.PyVIEW.PyVIEW_LEFT)
            cv2.imshow("ZED", mat.get_data())
            key = cv2.waitKey(5)
            settings(key, cam, runtime, mat)
        else:
            key = cv2.waitKey(5)
    cv2.destroyAllWindows()

    cam.close()
    print("\nFINISH")


def print_camera_information(cam):
    print("Resolution: {0}, {1}.".format(round(cam.get_resolution().width, 2), cam.get_resolution().height))
    print("Camera FPS: {0}.".format(cam.get_camera_fps()))
    print("Firmware: {0}.".format(cam.get_camera_information().firmware_version))
    print("Serial number: {0}.\n".format(cam.get_camera_information().serial_number))


def print_help():
    print("Help for camera setting controls")
    print("  Increase camera settings value:     +")
    print("  Decrease camera settings value:     -")
    print("  Switch camera settings:             s")
    print("  Reset all parameters:               r")
    print("  Record a video:                     z")
    print("  Quit:                               q\n")


def settings(key, cam, runtime, mat):
    if key == 115:  # for 's' key
        switch_camera_settings()
    elif key == 43:  # for '+' key
        current_value = cam.get_camera_settings(camera_settings)
        cam.set_camera_settings(camera_settings, current_value + step_camera_settings)
        print(str_camera_settings + ": " + str(current_value + step_camera_settings))
    elif key == 45:  # for '-' key
        current_value = cam.get_camera_settings(camera_settings)
        if current_value >= 1:
            cam.set_camera_settings(camera_settings, current_value - step_camera_settings)
            print(str_camera_settings + ": " + str(current_value - step_camera_settings))
    elif key == 114:  # for 'r' key
        cam.set_camera_settings(sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_BRIGHTNESS, -1, True)
        cam.set_camera_settings(sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_CONTRAST, -1, True)
        cam.set_camera_settings(sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_HUE, -1, True)
        cam.set_camera_settings(sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_SATURATION, -1, True)
        cam.set_camera_settings(sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_GAIN, -1, True)
        cam.set_camera_settings(sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_EXPOSURE, -1, True)
        cam.set_camera_settings(sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_WHITEBALANCE, -1, True)
        print("Camera settings: reset")
    elif key == 122:  # for 'z' key
        record(cam, runtime, mat)


def switch_camera_settings():
    global camera_settings
    global str_camera_settings
    if camera_settings == sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_BRIGHTNESS:
        camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_CONTRAST
        str_camera_settings = "Contrast"
        print("Camera settings: CONTRAST")
    elif camera_settings == sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_CONTRAST:
        camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_HUE
        str_camera_settings = "Hue"
        print("Camera settings: HUE")
    elif camera_settings == sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_HUE:
        camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_SATURATION
        str_camera_settings = "Saturation"
        print("Camera settings: SATURATION")
    elif camera_settings == sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_SATURATION:
        camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_GAIN
        str_camera_settings = "Gain"
        print("Camera settings: GAIN")
    elif camera_settings == sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_GAIN:
        camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_EXPOSURE
        str_camera_settings = "Exposure"
        print("Camera settings: EXPOSURE")
    elif camera_settings == sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_EXPOSURE:
        camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_WHITEBALANCE
        str_camera_settings = "White Balance"
        print("Camera settings: WHITEBALANCE")
    elif camera_settings == sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_WHITEBALANCE:
        camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_BRIGHTNESS
        str_camera_settings = "Brightness"
        print("Camera settings: BRIGHTNESS")


def record(cam, runtime, mat):
    vid = tp.PyERROR_CODE.PyERROR_CODE_FAILURE
    out = False
    while vid != tp.PyERROR_CODE.PySUCCESS and not out:
        filepath = input("Enter filepath name: ")
        vid = cam.enable_recording(filepath)
        print(repr(vid))
        if vid == tp.PyERROR_CODE.PySUCCESS:
            print("Recording started...")
            out = True
            print("Hit spacebar to stop recording: ")
            key = False
            while key != 32:  # for spacebar
                err = cam.grab(runtime)
                if err == tp.PyERROR_CODE.PySUCCESS:
                    cam.retrieve_image(mat)
                    cv2.imshow("ZED", mat.get_data())
                    key = cv2.waitKey(5)
                    cam.record()
        else:
            print("Help: you must enter the filepath + filename + SVO extension.")
            print("Recording not started.")
    cam.disable_recording()
    print("Recording finished.")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
