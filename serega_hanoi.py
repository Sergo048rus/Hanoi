import os
import hanoi_graph_mod as solver


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

        



    
    def condition_check(self):                          #выбор постоения пирамиды
        pass

    def sort_rod(self):                              # Соритруем штыри по стоимости
        rod_pyr_base = self.rodCost.pop(0)
        bubble_sort(self.rodCost)
        self.rodCost.insert(0,rod_pyr_base)          # отсортированная стоимость с зафиксирванным начальным штырем


    def solveGraph(self):               #Вызываем граф для итогого решения
        cost, path = solver.BuildPath(self.diskCount,self.rodCost,0,1)
        return cost, path

    def pyramid_3(self,dst_rod):                # Собираем пирамиду из 3 дисков на одном штыре 
        cost_dst, path_dst = solver.BuildPath(3,self.rodCost,0,dst_rod)
        cost_end, path_end = solver.BuildPath(3, self.rodCost, dst_rod, 1)
        cost = cost_end+cost_dst
        return cost, path_dst,path_end


    def pyramid_4(self,dst_rod):                # Собираем пирамиду из 4 дисков на одном штыре
        cost_dst, path_dst = solver.BuildPath(4, self.rodCost, 0, dst_rod)
        cost_end, path_end = solver.BuildPath(4, self.rodCost, dst_rod, 1)
        cost = cost_end+cost_dst
        return cost, path_dst,path_end
    
    def pyramid_5(self,dst_rod):                # Собираем пирамиду из 3 дисков на одном штыре 
        cost_dst, path_dst = solver.BuildPath(5, self.rodCost, 0, dst_rod)
        cost_end, path_end = solver.BuildPath(5, self.rodCost, dst_rod, 1)
        cost = cost_end+cost_dst
        return cost, path_dst,path_end

    def pyramid_6(self,dst_rod):                # Собираем пирамиду из 4 дисков на одном штыре
        cost_dst, path_dst = solver.BuildPath(6, self.rodCost, 0, dst_rod)
        cost_end, path_end = solver.BuildPath(6, self.rodCost, dst_rod, 1)
        cost = cost_end+cost_dst
        return cost, path_dst,path_end



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
        

