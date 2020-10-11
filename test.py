from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QSizePolicy

import sys
from Hanoi import *

from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
import InputTXT as parser



class Window(QMainWindow):
    def __init__(self,Hanoi):
        super().__init__()

        self.title = "Hanoi 2020 @Zavodnoi Apelsin"
        self.top = 100
        self.left = 100
        self.width = 1800
        self.heigth = 600
        
        self.Hanoi = Hanoi

        
    
    def InitWindow(self):

        scene = QGraphicsScene()
        
        redBrush = QBrush(Qt.red)
        blueBrush = QBrush(Qt.blue)
        
        blackPen = QPen(Qt.black)
        blackPen.setWidth(7)

        bluePen = QPen(Qt.blue)
        bluePen.setWidth(2)

        view = QGraphicsView(scene,self)
        view.setGeometry(0,0,1800,500)
        # view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.setWindowIcon(QtGui.QIcon("doc/apelsin.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.heigth)
        self.show()
       
        return scene
        # rect2 = Hanoi.disk_place(0,2,20,scene)

        # rect2 = Hanoi.disk_place(0,1,2,scene)
        # rect3 = Hanoi.disk_place(9,5,1,scene)
        # rect4 = Hanoi.disk_place(8,4,1,scene)
        # rect5 = Hanoi.disk_place(7,5,1,scene)
        # rect5 = Hanoi.disk_place(10,20,1,scene)
        # scene.removeItem(rect1)
        #disc_list[7] = Hanoi.disk_place(2,0,7,scene)



if __name__ == "__main__": 
    Hanoi = Hanoi()
    App = QApplication(sys.argv)
    window = Window(Hanoi)

    parser = parser.InputTXT()
    FILENAME = "tests_file/t3-3.txt" 

    numDisk, numColumn, Cost, err = parser.ReadDisk(FILENAME)
    
    scene = window.InitWindow()

    
           

    if err == 0:
        disc_list = Hanoi.StartInit(numDisk,numColumn,scene)

    order, sizeOrder, returnErr = parser.ReadOrder(FILENAME)
    
    
    if returnErr == 0 and err == 0:
        for i in range(0,sizeOrder):
            scene.removeItem(disc_list[order[i]['dI']])
                
            

        # disc_list[7] = Hanoi.disk_place(2,0,7,scene)


    sys.exit(App.exec())

