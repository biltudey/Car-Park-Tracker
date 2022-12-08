import cv2
import cvzone
import numpy as np
import pickle

cap = cv2.VideoCapture('carPark.mp4')

with open('carPark', 'rb') as f:
    posList=pickle.load(f)

width,height = 108,48

def checkparking(imgPros):
    spaceCounter = 0
    for pos in posList:
        x,y = pos
        # cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(0,0,255),2)
        # cv2.imshow('carpark',img)

        imgCrop = imgPros[y:y+height,x:x+height]
        # cv2.imshow(str(x*y),imgCrop)
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img,str(count),(x,y+height-10),1,2,( 0,255,0),offset=0)

        if count <205:
            color = (0,255,0)
            thickness = 5
            spaceCounter +=1
        else:
            color = (0,0,255)
            thickness = 2
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),color,thickness)
        cvzone.putTextRect(img,f'Free space {spaceCounter}/{len(posList)}',(200,50),2,2,( 0,200,0),offset=20)


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    succes,img = cap.read()

    imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imggray,(3,3),1)

    imgThreshold=cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold,5)

    kernel = np.zeros((3,3),np.uint8())
    imgDilate = cv2.dilate(imgMedian,kernel,iterations=1)

    checkparking(imgDilate)

    
        
    cv2.imshow('carpark',img)
    # cv2.imshow('Blur',imgBlur)
    # cv2.imshow('Threshold',imgThreshold)
    # cv2.imshow('Median',imgMedian)
    # cv2.imshow('imgDilate',imgDilate)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break