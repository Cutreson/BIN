import cv2
import numpy as np
import sqlite3
import os

def insertIntoDatabase(SoTu,ThoiGianGuiDo,ThoiGianLayDo,TrangThai):
    conn = sqlite3.connect("F:/QT/BIN/Demo/Ver_1/database.db")
    query = "INSERT INTO data (SoTu,ThoiGianGuiDo,ThoiGianLayDo,TrangThai) VALUES ("+str(SoTu) + ",'" + str(ThoiGianGuiDo) + "','" + str(ThoiGianLayDo) + "','" + str(TrangThai) +"')"
    conn.execute(query)
    conn.commit()
    conn.close() 
    ########################    
def updateIntoDatabase(ID,ThoiGianLayDo,TrangThai):
    conn = sqlite3.connect("F:/QT/BIN/Demo/Ver_1/database.db")
    query = "UPDATE data SET ThoiGianLayDo = '" + str(ThoiGianLayDo) + "','" + str(TrangThai) + "' WHERE ID = " + str(ID)
    conn.execute(query)
    conn.commit()
    conn.close() 
insertIntoDatabase(1,"8h00","9h00","Da Gui")
updateIntoDatabase(14,"15h00","Da Lay")