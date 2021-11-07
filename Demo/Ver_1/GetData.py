import cv2
import numpy as np
import sqlite3
import os

def insertIntoDatabase(ThoiGian,SoTu,TrangThai):
    conn = sqlite3.connect("F:/QT/BIN/Demo/Ver_1/database.db")
    query = "INSERT INTO data (ThoiGian,SoTu,TrangThai) VALUES ('" + str(ThoiGian) + "'," + str(SoTu) + ",'" +str(TrangThai) +"')"
    conn.execute(query)
    conn.commit()
    conn.close() 
    ########################    
insertIntoDatabase("Son",2,"Chua_lay")