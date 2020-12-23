
import sys
import os
import hanoi_graph_mod as solver
import copy

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


def sort_rod(rodCost):                              # Соритруем штыри по стоимости
    rod_pyr_base = rodCost.pop(0)
    bubble_sort(rodCost)
    rodCost.insert(0,rod_pyr_base)          # отсортированная стоимость с зафиксирванным начальным штырем


def solveGraph(diskCountCurr,rodCost):               #Вызываем граф для итогого решения
    cost, path = solver.BuildPath(diskCountCurr,rodCost,0,1,True)
    return cost, path

def pyramid_3(rodCost,dst_rod):                # Собираем пирамиду из 3 дисков на одном штыре 
    cost_dst, path_dst = solver.BuildPath(3,rodCost,0,dst_rod,False)
    cost_end, path_end = solver.BuildPath(3, rodCost, dst_rod, 1,False)
    cost = cost_end+cost_dst
    return cost, path_dst,path_end


def pyramid_4(rodCost,dst_rod):                # Собираем пирамиду из 4 дисков на одном штыре
    cost_dst, path_dst = solver.BuildPath(4, rodCost, 0, dst_rod,False)
    cost_end, path_end = solver.BuildPath(4, rodCost, dst_rod, 1,False)
    cost = cost_end+cost_dst
    return cost, path_dst,path_end

def pyramid_5(rodCost,dst_rod):                # Собираем пирамиду из 3 дисков на одном штыре 
    cost_dst, path_dst = solver.BuildPath(5, rodCost, 0, dst_rod,False)
    cost_end, path_end = solver.BuildPath(5, rodCost, dst_rod, 1,False)
    cost = cost_end+cost_dst
    return cost, path_dst,path_end

def pyramid_6(rodCost,dst_rod):                # Собираем пирамиду из 4 дисков на одном штыре
    cost_dst, path_dst = solver.BuildPath(6, rodCost, 0, dst_rod,False)
    cost_end, path_end = solver.BuildPath(6, rodCost, dst_rod, 1,False)
    cost = cost_end+cost_dst
    return cost, path_dst,path_end

def pyramid_xx(diskCount,rodCost,dst_rod,pyr1,pyr2):
    
    cost = 0
    cost_1 = 0
    path_dst =[]
    path_dst_1 = []
    path_end = []
    path_end_1 = []

    sw = StopWatch()
    
    if pyr1 == 6:
        cost,path_dst,path_end = pyramid_6(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=6
    elif pyr1 == 5:
        cost,path_dst,path_end = pyramid_5(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=5
    elif pyr1 == 4:
        cost,path_dst,path_end = pyramid_4(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=4
    elif pyr1 == 3:
        cost,path_dst,path_end = pyramid_3(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=3

    if pyr2 == 6:
        cost_1,path_dst_1,path_end_1 = pyramid_6(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=6
    elif pyr2 == 5:
        cost_1,path_dst_1,path_end_1 = pyramid_5(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=5
    elif pyr2 == 4:
        cost_1,path_dst_1,path_end_1 = pyramid_4(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=4
    elif pyr2 == 3:
        cost_1,path_dst_1,path_end_1 = pyramid_3(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=3

    cost+=cost_1
    path_dst += path_dst_1
    path_end += path_end_1

    sw.stop()
    return cost,path_dst,path_end,diskCount

def hanoi_gr_pre(diskCount, rodCostList,dst_rod):
    
    rodCount = len(rodCostList)
    rodCost = rodCostList


    sort_rod(rodCost)

    print(rodCost)
    rodCost_sort = copy.deepcopy(rodCost)
    if len(rodCost_sort) > 3 and diskCount > 6:
        for stage in range(14):
            rodCost = copy.deepcopy(rodCost_sort)

            cost = 0
            path = []
            cost_pyro,path_dst,path_end,diskCountCurr = condition_check(diskCount,rodCost,dst_rod,stage)              # необходимо разобрться какие условия и сколько строить башен
            if(diskCountCurr<diskCount):                                                                              # Вместо ERR если диски не уменьшились значит вывелось число с ошибкой
                cost_graph, path_graph = solveGraph(diskCountCurr,rodCost)

                cost = cost_pyro + cost_graph
                path = path_dst+path_graph+path_end
                print(cost, path)
            
                # один формат наш, другой Васекина, можно оставить любой или выпилить все для скорости
                exportPath1 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path.txt".format(FILENAME.split('.')[0])))
                exportPath2 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path2.txt".format(FILENAME.split('.')[0])))
                solver.exportPathToFile(exportPath1, path, cost)
                # exportPathToFileAlternate(exportPath2, path, cost)

                print("Total cost: {0}".format(cost))

    else:           # Альтернатвное решение без подбашен
        cost, path = solveGraph(rodCost_sort,rodCost)

        print(cost, path)
        
        # один формат наш, другой Васекина, можно оставить любой или выпилить все для скорости
        exportPath1 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path.txt".format(FILENAME.split('.')[0])))
        exportPath2 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path2.txt".format(FILENAME.split('.')[0])))
        solver.exportPathToFile(exportPath1, path, cost)
        # exportPathToFileAlternate(exportPath2, path, cost)

        print("Total cost: {0}".format(cost))



    
def condition_check(diskCount,rodCost,dst_rod,stage):                          #выбор постоения пирамиды
    while len(rodCost)>diskCount:                                # Убираем самые дорогие штыри пока количество штыре не будет равно или меньше дисков
        rodCost.pop()
    if stage == 0:
        if diskCount < 11:
            cost,path_dst,path_end = pyramid_3(rodCost,dst_rod)
            rodCost.pop(dst_rod)
            diskCount-=3
            return cost,path_dst,path_end,diskCount
        else:
            print('STAGE 0: ERR count disk')
    if stage == 1:
        if diskCount > 8 and diskCount < 13:
            cost,path_dst,path_end = pyramid_4(rodCost,dst_rod)
            rodCost.pop(dst_rod)
            diskCount-=4
            return cost,path_dst,path_end,diskCount
        else:
            print('STAGE 1: ERR count disk')
    if stage == 2:
        if (diskCount > 9 and diskCount < 14) or len(rodCost)==4:
            cost,path_dst,path_end = pyramid_5(rodCost,dst_rod)
            rodCost.pop(dst_rod)
            diskCount-=5
            return cost,path_dst,path_end,diskCount
        else:
            print('STAGE 2: ERR count disk')
    if stage == 3:
        if (diskCount > 9 and diskCount < 15) or len(rodCost)==4:                
            cost,path_dst,path_end = pyramid_6(rodCost,dst_rod)
            rodCost.pop(dst_rod)
            diskCount-=6
            return cost,path_dst,path_end,diskCount
        else:
            print('STAGE 3: ERR count disk')
    if stage == 4:
        if diskCount > 15:
            return pyramid_xx(diskCount,rodCost,dst_rod,6,6)
        else:
            print('STAGE 4: ERR count disk')
    if stage == 5:
        if diskCount > 14:
            return pyramid_xx(diskCount,rodCost,dst_rod,6,5)
        else:
            print('STAGE 5: ERR count disk')
    if stage == 6:
        if diskCount > 13 and diskCount < 17:
            return pyramid_xx(diskCount,rodCost,dst_rod,6,4)
        else:
            print('STAGE 6: ERR count disk')
    if stage == 7:
        if diskCount > 12 and diskCount < 16:
            return pyramid_xx(diskCount,rodCost,dst_rod,6,3)
        else:
            print('STAGE 7: ERR count disk')
    if stage == 8:
        if diskCount > 14 and diskCount < 17:
           return pyramid_xx(diskCount,rodCost,dst_rod,5,5)
        else:
            print('STAGE 8: ERR count disk')
    if stage == 9:
        if diskCount > 13  and diskCount < 17:
           return pyramid_xx(diskCount,rodCost,dst_rod,5,4)
        else:
            print('STAGE 9: ERR count disk')
    if stage == 10:
        if diskCount > 12  and diskCount < 16:
           return pyramid_xx(diskCount,rodCost,dst_rod,5,3)
        else:
            print('STAGE 10: ERR count disk')
    if stage == 11:
        if diskCount > 10 and diskCount < 16:
           return pyramid_xx(diskCount,rodCost,dst_rod,4,4)
        else:
            print('STAGE 11: ERR count disk')
    if stage == 12:
        if diskCount > 9 and diskCount < 17:
           return pyramid_xx(diskCount,rodCost,dst_rod,4,3)
        else:
            print('STAGE 12: ERR count disk')
    if stage == 13:
        if diskCount > 8 and diskCount < 16:
           return pyramid_xx(diskCount,rodCost,dst_rod,3,3)
        else:
            print('STAGE 13: ERR count disk')

    cost = 0
    path_dst = []
    path_end = []
    return cost,path_dst,path_end,diskCount









if __name__ == "__main__": 
    FOLDERNAME = "solver_test/"
    FILENAME = "8d6r.txt" 
    

    dst_rod = 3


    if len(sys.argv) < 3:
        print("WARN! Use predefined value!")   
    else:
        if "hanoi_graph.py" in str(sys.argv[1]):
            print("WARN! Detect VS Code, use predefined value!")
        else:
            FILENAME = str(sys.argv[1])
            dst_rod = int(sys.argv[2])


    FILEPATH = FOLDERNAME + FILENAME
    import InputTXT as par
    parser = par.InputTXT()

    diskCount, column, diskCost, err = parser.ReadDisk(FILEPATH)
    print('TESTFILE: %s' % (FILEPATH))
    print(' DiskCount = ',diskCount,'\n','Column = ', column,'\n','Err = ', err,'\n', 'Cost', diskCost)

    # order, sizeOrder, returnErr = parser.ReadOrder(FILENAME)
    if err == 'OK':
        sw = StopWatch()
        hanoi_gr_pre(diskCount, diskCost,dst_rod)
        sw.stop()

        

