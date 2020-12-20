import os
import networkx as nx
import matplotlib.pyplot as plt 

from stopwatch import StopWatch

def bubble_sort(nums):  
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


class hanoi_gr_pre():
    def __init__(self, diskCount, rodCostList):
        self.diskCount_base = diskCount
        self.diskCount = diskCount

        self.diskRange_base = range(0,diskCount)

        self.rodCount = len(rodCostList)
        self.rodCost = rodCostList
        self.rodCost_base = rodCostList
        self.rodRange = range(0,self.rodCount)

        self.orderCost = 0
        self.orderPath = []

        self.pyramidBildCost = []

        self.sort_rod()
        self.condition_check()              # необходимо разобрться какие условия и сколько строить башен
        




        #-------------------------------------------------------
        # Сделали несколько башен уменьшили диски строим граф


        #-------------------------------------------------------

        



    
    def condition_check(self):                  #выбор постоения пирамиды
        while self.rodCount > 3 and self.diskCount > 7:
            if self.diskCount > 7 and self.diskCount <= 20:
                self.pyramid_3()
            # if self.diskCount > 9 and self.diskCount < 14:
            #     self.pyramid_4()

    def sort_rod(self):                 # Соритруем штыри по стоимости
        rod_pyr_base = self.rodCost.pop(0)
        bubble_sort(self.rodCost)
        self.rodCost.insert(0,rod_pyr_base)          # отсортированная стоимость с зафиксирванным начальным штырем



    def pyramid_3(self):                # Собираем пирамиду из 3 дисков на одном штыре 
                                        # По фиксированному пути считаем стоимость 0->1 0->2 0->3 2->3 1->3
        self.orderCost += self.rodCost[1]+self.rodCost[2]+3*self.rodCost[3]
                                        # Плюс стоимость разборки пирамиды 
                                        # 3->4 3->2 3->1 2->1 4->1
        if self.rodCount > 4 and (self.rodCost[0]>self.rodCost[4]) and (self.rodCost[1]+self.rodCost[2]+self.rodCost[3] > self.rodCost[4]):     
            self.orderCost += self.rodCost[4]+self.rodCost[2]+3*self.rodCost[1]
                                        # 3->1 3->2 1->2 3->1 2->3 2->1 3->1 #!НЕВЕРНО
        elif (self.rodCost[0]>self.rodCost[1]+self.rodCost[2]+self.rodCost[3]):                                                          
            self.orderCost += 4*self.rodCost[1]+2*self.rodCost[2]+self.rodCost[3]
        else:                           # 3->0 3->2 3->1 2->1 0->1
            self.orderCost += self.rodCost[0]+self.rodCost[2]+3*self.rodCost[1]
            
        rod_pyr = self.rodCost.pop(3)               #выпиливаем штырь
        self.pyramidBildCost.insert(0,rod_pyr)      #сохраняем стоимость выпилиного 
        self.diskCount -= 3                         # Забываем про 3 диска
        self.rodCount = len(self.rodCost)


        print('-----------------')
        print('Кол дисков:\t',self.diskCount)
        print('Кол штырей:\t',self.rodCount)
        print('Цена штырей:\t',self.rodCost)
        print('Стоимость:\t',self.orderCost,'\n')


    def pyramid_4(self):                # Собираем пирамиду из 4 дисков на одном штыре
        pass
    




if __name__ == "__main__": 
    FOLDERNAME = "solver_test/"
    FILENAME = "8d4r.txt" 
    FILEPATH = FOLDERNAME + FILENAME

    import InputTXT as par
    parser = par.InputTXT()

    diskCount, column, diskCost, err = parser.ReadDisk(FILEPATH)
    print('TESTFILE: %s' % (FILEPATH))
    print(' DiskCount = ',diskCount,'\n','Column = ', column,'\n','Err = ', err,'\n', 'Cost', diskCost)

    # order, sizeOrder, returnErr = parser.ReadOrder(FILENAME)
    if err == 'OK':
        sw = StopWatch()
        graph = hanoi_gr_pre(diskCount, diskCost)
        sw.stop()
        

