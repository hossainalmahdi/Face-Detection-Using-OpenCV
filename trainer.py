import cv2
import os
import numpy as np
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'DataSet'

def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return IDs,faces
faces,Ids = getImagesWithID('DataSet')
recognizer.train(faces,np.array(IDs))
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()