import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'DIVX') #for windows
out=cv2.VideoWriter('output.mkv',fourcc, 20.0, (640,480)) #20 means fps
while True:
    retrn,frame = cap.read()  #so here must be two variables one for return and another is frame
    cv2.imshow('frame',frame)
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('rgb',rgb)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
