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
    pErrorx, pErrory = trackFace(drone, info, 360, 240, pidx, pidy, pErrorx, pErrory)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        drone.land()
        break


# from utils import *
# import cv2
 
# w,h = 360,240
# pid = [0.4,0.4,0]
# pError = 0
# startCounter = 0  # for no Flight 1   - for flight 0
 
 
# myDrone = initializeTello()
 
# while True:
 
#     ## Flight
#     if startCounter == 0:
#         myDrone.takeoff()
#         startCounter = 1
 
#     ## Step 1
#     img = telloGetFrame(myDrone,w,h)
#     ## Step 2
#     img, info = findFace(img)
#     ## Step 3
#     pError = trackFace(myDrone,info,w,pid,pError)
#     #print(info[0][0])
#     cv2.imshow('Image',img)
#     if cv2.waitKey(1) and 0xFF == ord('q'):
#         myDrone.land()
#         break
