from PyQt5 import QtGui
# from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QSizePolicy, QPushButton, QLineEdit,QFileDialog,QTextEdit

import sys
from Hanoi import *

from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
import InputTXT as par



class Window(QMainWindow):
    def __init__(self,Hanoi):
        super().__init__()

        self.title = "Hanoi 2020 @Zavodnoi Apelsin"
        self.top = 100
        self.left = 100
        self.width = 1800
        self.heigth = 800
        
        self.Hanoi = Hanoi
        self.parser = par.InputTXT()
        self.InitWindow()

        
    
    def InitWindow(self):

        self.scene = QGraphicsScene()
        
        redBrush = QBrush(Qt.red)
        blueBrush = QBrush(Qt.blue)
        
        blackPen = QPen(Qt.black)
        blackPen.setWidth(7)

        bluePen = QPen(Qt.blue)
        bluePen.setWidth(2)

        view = QGraphicsView(self.scene,self)
        view.setGeometry(0,0,1800,500)
        # view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.setWindowIcon(QtGui.QIcon("doc/apelsin.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.heigth)
        
       
        #-----------------------------------------------------------------------------------------------------------
        #Определяем кнопки

        btn1 = QPushButton("Start order", self)
        btn1.setGeometry(30, 510,100,30)

        btn2 = QPushButton("Start optimization", self)
        btn2.setGeometry(150, 510,100,30)

        btn3 = QPushButton("Step back", self)
        btn3.setGeometry(150, 545,100,30)

        btn4 = QPushButton("Step forward", self)
        btn4.setGeometry(30, 545,100,30)

        btnFile = QPushButton("File...", self)
        btnFile.setGeometry(605, 510,100,30)


        btn1.clicked.connect(self.startOrderClicked)
        btn2.clicked.connect(self.startOptimClicked)
        btn3.clicked.connect(self.stepOrderBack)
        btn4.clicked.connect(self.stepOrderForward)
        btnFile.clicked.connect(self.getFile)
        #-----------------------------------------------------------------------------------------------------------
        #Определяем lineEdit
        self.qle = QLineEdit(self)
        # qle.move(300, 510)
        self.qle.setGeometry(300, 511,300,28)
        #-----------------------------------------------------------------------------------------------------------
        #Типа консоль
        self.Console = QTextEdit(self)
        self.Console.setGeometry(720, 510,500,250)
        self.show()
        
        # rect2 = Hanoi.disk_place(0,2,20,scene)

        # rect2 = Hanoi.disk_place(0,1,2,scene)
        # rect3 = Hanoi.disk_place(9,5,1,scene)
        # rect4 = Hanoi.disk_place(8,4,1,scene)
        # rect5 = Hanoi.disk_place(7,5,1,scene)
        # rect5 = Hanoi.disk_place(10,20,1,scene)
        # scene.removeItem(rect1)
        #disc_list[7] = Hanoi.disk_place(2,0,7,scene)
    
    def startOrderClicked(self):
        numDisk, numColumn, Cost, err = self.parser.ReadDisk(self.filename)
    
        if err == 'OK':
            disc_list = Hanoi.StartInit(numDisk,numColumn,self.scene)

        order, sizeOrder, returnErr = self.parser.ReadOrder(self.filename)

    def startOptimClicked(self):
        pass

    def stepOrderForward(self):
        pass

    def stepOrderBack(self):
        pass

    def getFile(self):                                                     
        self.filename, self.filetype = QFileDialog.getOpenFileName(self,
                             "Выбрать файл",
                             ".",
                             "Text Files(*.txt);;All Files(*)")
        self.qle.setText((self.filename))


if __name__ == "__main__": 
    Hanoi = Hanoi()
    App = QApplication(sys.argv)
    window = Window(Hanoi)

   
    

    
    
    
    # if returnErr == 0 and err == 0:
    #     for i in range(0,sizeOrder):
    #         scene.removeItem(disc_list[order[i]['dI']])
                
            

        # disc_list[7] = Hanoi.disk_place(2,0,7,scene)


    sys.exit(App.exec())

