#Anuj Vasil & Devin Mui
#CSCI 513 USC
#Autonomous Cinema Drone

from utils import *
import cv2


pErrorx = 0
pErrory = 0
start = 0
pidx = [0.5,0.5,0]
pidy = [0.5,0.5,0]

drone = initDrone()
while True:

    if start == 0:
        drone.takeoff()
        drone.move_up(60)
        start = 1

    img = getFrame(drone)

    img, info = findFace(img)
    pErrorx, pErrory = trackFace(drone, info, 360, 240, pidx, pidy, pErrorx, pErrory)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        drone.land()
        break
