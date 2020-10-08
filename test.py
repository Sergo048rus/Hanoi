from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QSizePolicy

import sys
from Hanoi import *

from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt




class Window(QMainWindow):
    def __init__(self,Hanoi):
        super().__init__()

        self.title = "Hanoi 2020 @Zavodnoi Apelsin"
        self.top = 100
        self.left = 100
        self.width = 1800
        self.heigth = 600
        
        self.Hanoi = Hanoi

        self.InitWindow()
    
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
        
        

        
        # Hanoi.disk_place(0,2,4,scene)
        
        # rect1 = scene.addRect(100,0,2,420,bluePen,blueBrush)

        disc_list = Hanoi.StartInit(20,10,scene)

        # scene.removeItem(disc_list[7])
        # disc_list[7] = Hanoi.disk_place(2,0,7,scene)
        # rect2 = Hanoi.disk_place(0,2,20,scene)

        # rect2 = Hanoi.disk_place(0,1,2,scene)
        rect3 = Hanoi.disk_place(9,5,1,scene)
        rect4 = Hanoi.disk_place(8,4,1,scene)
        rect5 = Hanoi.disk_place(7,5,1,scene)
        rect5 = Hanoi.disk_place(10,20,1,scene)
        # scene.removeItem(rect1)

        # spisok_rect = [rect,rect1]
        # scene.removeItem(spisok_rect[0])

        self.setWindowIcon(QtGui.QIcon("apelsin.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.heigth)
        self.show()




Hanoi = Hanoi()
App = QApplication(sys.argv)
window = Window(Hanoi)
sys.exit(App.exec())

