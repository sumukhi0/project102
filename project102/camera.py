from pickle import FALSE
import cv2

def picture():
    cam = cv2.VideoCapture(0)
    result = True
    while(result):
        p, Img = cam.read()
        cv2.imwrite("Img.png",Img)
        result = False

    cam.relase()
    cv2.destroyAllWindows()    

picture()