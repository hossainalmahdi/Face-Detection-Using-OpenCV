import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(2)
id = input('Please Register your Identity here')
snum = 0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        snum = snum + 1
        cv2.imwrite("DataSet/user." + str(id) + "." + str(snum) + ".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.waitKey(100)

    cv2.imshow('img', img)
    cv2.waitKey(1)
    if snum > 20:
        break

cap.release()
cv2.destroyAllWindows()
