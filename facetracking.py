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
        drone.move_up(80)
        start = 1

    img = getFrame(drone)

    img, info = findFace(img)
    pErrorx, pErrory = trackFace(drone, info, 640, 480, pidx, pidy, pErrorx, pErrory)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        break
