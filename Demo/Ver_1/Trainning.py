import cv2
import numpy as np
import os
from PIL import Image

url = "F:/QT/BIN/Demo/Ver_1/"
path = url + "dataSet"

def getImageWithSoTu(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    #print(imagePaths)
    faces = []
    SoTus = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert("L")
        faceNp = np.array(faceImg,"uint8")
        #print(faceNp)
        SoTu = int(imagePath.split("\\")[1].split(".")[1])
        faces.append(faceNp)
        SoTus.append(SoTu)
        cv2.imshow("trainning",faceNp)
        cv2.waitKey(5)
    cv2.destroyAllWindows()
    return faces, SoTus

def trainData():
    faces, SoTus =  getImageWithSoTu(path)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(SoTus))
    if not os.path.exists(url + "recoginizer"):
        os.makedirs(url + "Ver_1/recoginizer")
    recognizer.save(url + "recoginizer/trainningData.yml")

trainData()