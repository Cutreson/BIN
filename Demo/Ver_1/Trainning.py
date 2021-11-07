import cv2
import numpy as np
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "F:/QT/BIN/Demo/Ver_1/dataSet"

def getImageWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    #print(imagePaths)
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert("L")
        faceNp = np.array(faceImg,"uint8")
        #print(faceNp)
        Id = int(imagePath.split("\\")[1].split(".")[1])
        faces.append(faceNp)
        IDs.append(Id)
        
        cv2.imshow("trainning",faceNp)
        cv2.waitKey(10)
    return faces, IDs

faces, IDs =  getImageWithID(path)
recognizer.train(faces, np.array(IDs))
if not os.path.exists("F:/QT/BIN/Demo/Ver_1/recoginizer"):
    os.makedirs("F:/QT/BIN/Demo/Ver_1/recoginizer")
recognizer.save("F:/QT/BIN/Demo/Ver_1/recoginizer/trainningData.yml")
cv2.destroyAllWindows()
