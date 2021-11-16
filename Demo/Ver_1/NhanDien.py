import cv2
import numpy as np
import os
import sqlite3
from PIL import Image

url = "F:/QT/BIN/Demo/Ver_1/"
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read(url + "recoginizer/trainningData.yml")
def getProfile(SoTu):
    conn = sqlite3.connect(url + "database.db")
    query = "SELECT * FROM data WHERE SoTu = " + str(SoTu)
    cusror = conn.execute(query)
    profile = None
    for row in cusror:
        profile = row
    conn.close()
    return profile
############################################################

def nhanDien():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        roi_gray = gray[y:y+h,x:x+w]
        SoTu,confidence = recognizer.predict(roi_gray)
        if confidence < 70:
            profile = getProfile(SoTu)
            if(profile != None):
                print("True")
                cap.release()
                return True
        else:
            print("False")
            cap.release()
            return False

#####################################################
nhanDien()

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        roi_gray = gray[y:y+h,x:x+w]
        SoTu,confidence = recognizer.predict(roi_gray)
        if confidence < 70:
            profile = getProfile(SoTu)
            if(profile != None):
                cv2.putText(frame,""+str(profile[1]), (x+10,y+h+30), cv2.FONT_ITALIC, 1, (0,255,0),2)
        else:
            cv2.putText(frame,"Unknow", (x+10,y+h+30), cv2.FONT_ITALIC, 1, (0,0,255),2)
    cv2.imshow("image",frame)
    if(cv2.waitKey(1) == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()