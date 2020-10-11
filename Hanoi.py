HANOI_MAX_COLUMN = 10
HANOI_MAX_DISK   = 20

from PyQt5.QtGui import QBrush, QPen, QColor
from PyQt5.QtCore import Qt

class Hanoi():
    def __init__(self):
     
        self.WIDTH_BASE_DISCK = 150
        self.HEIGTH_BASE_DISK = 20
        self.WIDTH_DISK_COEFF = 0.1
        self.HANOI_COLUMN_STEP = 160
        self.HANOI_COLUMN_BASE = 100

                
    def disk_width_init(self,num_disk):
        num_disk_width = self.WIDTH_BASE_DISCK
        num_disk = num_disk + 1
        for i in range(1,num_disk):
            num_disk_width=num_disk_width - num_disk_width*self.WIDTH_DISK_COEFF
        
        return num_disk_width
    
    def column_place(self,column_num):
        column_num_place = self.HANOI_COLUMN_BASE

        for i in range(1,column_num):
            column_num_place=column_num_place+self.HANOI_COLUMN_STEP
        
        return column_num_place
        

    # x_place == номеру столбца - столбец, в котором отрисовать диск
    # y_place - строка, в которой отрисовть диск. Равна произведению толщины диска на номер строки
    def disk_place(self,x_place,y_place,num_disk,scene):
        redBrush = QBrush(Qt.red)
        blueBrush = QBrush(QColor(0,250,0))
        
        blackPen = QPen(Qt.black)
        blackPen.setWidth(1)
        
        if num_disk%2 == 0:
            returnBrush = redBrush
        else:
            returnBrush =  blueBrush
        
        width_disk = self.disk_width_init(num_disk)
        top_place = self.column_place(x_place) - width_disk/2
        down_place = (20-y_place) * self.HEIGTH_BASE_DISK
        heigth_disk = self.HEIGTH_BASE_DISK
        
        rect = scene.addRect(top_place,down_place, width_disk,heigth_disk,blackPen, returnBrush)
        return rect

    def StartInit(self, num_disk, column_num,scene):
        blueBrush = QBrush(Qt.blue)
        bluePen = QPen(Qt.blue)
        bluePen.setWidth(2)

        disk_list = [0]*num_disk

        for i in range(1,column_num+1):
            col = self.column_place(i)
            scene.addRect(col,0,2,420,bluePen,blueBrush)
        for i in range(0,num_disk):
            disk_list[i] = self.disk_place(0,i,i,scene)
        
        return disk_list

