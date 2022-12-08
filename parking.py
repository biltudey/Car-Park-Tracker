import cv2
import pickle

# img = cv2.imread(r'carParkImg.png')
# img = cv2.resize(img,(500,500))
width,height = 108,48
try:
    with open('carPark', 'rb') as f:
        posList=pickle.load(f)
except:
    posList = []


def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i ,pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
    with open('carPark', 'wb') as f:
        pickle.dump(posList,f)




# cv2.rectangle(img,(58,192),(158,240),(255,0,255),2)

while True:
    img = cv2.imread(r'carParkImg.png')


    for pos in posList:

        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(0,0,255),2)
    cv2.imshow('image',img)
    cv2.rectangle(img,(58,192),(158,240),(255,0,255),2)

    cv2.setMouseCallback('image',mouseClick)
    cv2.waitKey(1)