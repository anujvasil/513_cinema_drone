from djitellopy import Tello
import cv2
import numpy as np

def initDrone():
    drone = Tello()
    drone.connect()
    print(drone.get_battery)
    drone.streamoff()
    drone.streamon()
    return drone

def getFrame(drone, w = 640, h = 480):
    frame = drone.get_frame_read()
    frame= frame.frame
    img = cv2.resize(frame, (w, h))
    return img

def findFace(img):
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 6)

    myFaceListC = []
    myFaceListArea = []
 
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cx = x + w//2
        cy = y + h//2
        area = w*h
        myFaceListArea.append(area)
        myFaceListC.append([cx,cy])
 
    if len(myFaceListArea) !=0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i],myFaceListArea[i]]
    else:
        return img,[[0,0],0] 


def trackFace(drone, info, w, h, pidx, pidy, pErrorx, pErrory):
    ## PID
    errorx = info[0][0] - w//2
    errory = info[0][1] - h//2
    speedx = pidx[0]*errorx + pidx[1]*(errorx-pErrorx)
    speedx = int(np.clip(speedx,-100,100))
    speedy = pidy[0]*errory + pidy[1]*(errory-pErrory)
    speedy = int(np.clip(speedy,-100,100))
 
 
    print(speedx)
    print(speedy)
    if info[0][0] != 0 and info[0][1] != 0:
        drone.yaw_velocity = speedx
        drone.up_down_velocity = speedy
    else:
        drone.for_back_velocity = 0
        drone.left_right_velocity = 0
        drone.up_down_velocity = 0
        drone.yaw_velocity = 0
        errorx = 0
        errory = 0
    if drone.send_rc_control:
        drone.send_rc_control(drone.left_right_velocity,
                                drone.for_back_velocity,
                                drone.up_down_velocity,
                                drone.yaw_velocity)
    return [errorx, errory]

