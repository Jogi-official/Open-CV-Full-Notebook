import cv2 as cv

cap = cv.VideoCapture(0)

#tracker = cv.TrackerMOSSE_create() # speed is high but not the accuracy

tracker =cv.TrackerCSRT_create() #speed is less but the accuracy is high

success , img = cap.read()
bbox = cv.selectROI("Tracking" , img , False)
tracker.init(img ,bbox)

def drawbox(img , bbox):
    x , y , w , h = int(bbox[0]) ,int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv.rectangle(img , (x,y) ,(x + w , y+h ) , (255 , 0 , 255) , 3  , 1)
    cv.putText(img, "Tracking ", (75, 75), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


while(True):
    timer =cv.getTickCount()
    success , img = cap.read()

    success , bbox =tracker.update(img)
    if success:
        drawbox(img ,bbox)
    else:
        cv.putText(img, "Lost ", (75 , 75), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    fps = cv.getTickFrequency() / (cv.getTickCount() - timer)
    cv.putText(img , str(int(fps)) , (75 , 50 ) , cv.FONT_HERSHEY_SIMPLEX ,0.7  ,(0 ,0 , 255) , 2)
    cv.imshow("Tracking" ,img)

    if(cv.waitKey(1) & 0xff == ord('q')):
        break