
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

def pyramid_5(rodCost,dst_rod):                # Собираем пирамиду из 5 дисков на одном штыре 
    cost_dst, path_dst = solver.BuildPath(5, rodCost, 0, dst_rod,False)
    cost_end, path_end = solver.BuildPath(5, rodCost, dst_rod, 1,False)
    cost = cost_end+cost_dst
    return cost, path_dst,path_end

def pyramid_6(rodCost,dst_rod):                # Собираем пирамиду из 6 дисков на одном штыре
    cost_dst, path_dst = solver.BuildPath(6, rodCost, 0, dst_rod,False)
    cost_end, path_end = solver.BuildPath(6, rodCost, dst_rod, 1,False)
    cost = cost_end+cost_dst
    return cost, path_dst,path_end

def pyramid_7(rodCost,dst_rod):                # Собираем пирамиду из 7 дисков на одном штыре
    cost_dst, path_dst = solver.BuildPath(7, rodCost, 0, dst_rod,False)
    cost_end, path_end = solver.BuildPath(7, rodCost, dst_rod, 1,False)
    cost = cost_end+cost_dst
    return cost, path_dst,path_end

def pyramid_8(rodCost,dst_rod):                # Собираем пирамиду из 8 дисков на одном штыре
    cost_dst, path_dst = solver.BuildPath(8, rodCost, 0, dst_rod,False)
    cost_end, path_end = solver.BuildPath(8, rodCost, dst_rod, 1,False)
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
    if pyr1 == 8:
        cost,path_dst,path_end = pyramid_8(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=8
    elif pyr1 == 7:
        cost,path_dst,path_end = pyramid_7(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=7
    elif pyr1 == 6:
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

    if pyr2 == 8:
        cost_1,path_dst_1,path_end_1 = pyramid_8(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=8
    elif pyr2 == 7:
        cost_1,path_dst_1,path_end_1 = pyramid_7(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=7
    elif pyr2 == 6:
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


def pyramid_xxx(diskCount,rodCost,dst_rod,pyr1,pyr2,pyr3):
    
    cost = 0
    cost_1 = 0
    cost_2 = 0
    path_dst =[]
    path_dst_1 = []
    path_dst_2 = []
    path_end = []
    path_end_1 = []
    path_end_2 = []

    sw = StopWatch()
    if pyr1 == 8:
        cost,path_dst,path_end = pyramid_8(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=8
    elif pyr1 == 7:
        cost,path_dst,path_end = pyramid_7(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=7
    elif pyr1 == 6:
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

    if pyr2 == 8:
        cost_1,path_dst_1,path_end_1 = pyramid_8(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=8
    elif pyr2 == 7:
        cost_1,path_dst_1,path_end_1 = pyramid_7(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=7
    elif pyr2 == 6:
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

    if pyr3 == 8:
        cost_2,path_dst_2,path_end_2 = pyramid_8(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=8
    elif pyr3 == 7:
        cost_2,path_dst_2,path_end_2 = pyramid_7(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=7
    elif pyr3 == 6:
        cost_2,path_dst_2,path_end_2 = pyramid_6(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=6
    elif pyr3 == 5:
        cost_2,path_dst_2,path_end_2 = pyramid_5(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=5
    elif pyr3 == 4:
        cost_2,path_dst_2,path_end_2 = pyramid_4(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=4
    elif pyr3 == 3:
        cost_2,path_dst_2,path_end_2 = pyramid_3(rodCost,dst_rod)
        rodCost.pop(dst_rod)
        diskCount-=3

    cost+=cost_1 + cost_2
    path_dst += path_dst_1 + path_dst_2
    path_end += path_end_1 + path_end_2

    sw.stop()
    return cost,path_dst,path_end,diskCount


def hanoi_gr_pre(diskCount, rodCostList,dst_rod,stage_param):
    __maxStage = 27
    if stage_param == 1:
        range_maxStage = range(0,int(__maxStage/2))
    elif stage_param == 2:
        range_maxStage = range(__maxStage/2,__maxStage)
    elif stage_param == 3:
        range_maxStage = range(__maxStage-5,__maxStage)
    elif stage_param == 4:
        range_maxStage = range(20,__maxStage)
    elif stage_param > 100 and stage_param < 100+__maxStage+1:
        range_maxStage = range(stage_param-101,stage_param-100)
    else:
       range_maxStage = range(0,__maxStage)
    rodCount = len(rodCostList)
    rodCost = rodCostList

    stageCost = [0 for _ in range(0,__maxStage)]

    sort_rod(rodCost)

    print(rodCost)
    rodCost_sort = copy.deepcopy(rodCost)
    if len(rodCost_sort) > 3 and diskCount > 6:
        for stage in range_maxStage:
            rodCost = copy.deepcopy(rodCost_sort)
            sw_stage = StopWatch()
            cost = 0
            path = []
            cost_pyro,path_dst,path_end,diskCountCurr = condition_check(diskCount,rodCost,dst_rod,stage)              # необходимо разобрться какие условия и сколько строить башен
            if(diskCountCurr<diskCount):                                                                              # Вместо ERR если диски не уменьшились значит вывелось число с ошибкой
                cost_graph, path_graph = solveGraph(diskCountCurr,rodCost)

                cost = cost_pyro + cost_graph
                path = path_dst+path_graph+path_end
                print(cost, path)
                stageCost[stage] = cost
                sw_stage.stop()
                # один формат наш, другой Васекина, можно оставить любой или выпилить все для скорости
                FILENAME_OUT = FILENAME.split('.')[0]+'_'+str(dst_rod)+'_'+str(stage)
                exportPath1 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path.txt".format(FILENAME_OUT)))
                exportPath2 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path2.txt".format(FILENAME_OUT)))
                solver.exportPathToFile(exportPath1, path, cost)
                # exportPathToFileAlternate(exportPath2, path, cost)

                print("Total cost: {0}".format(cost))
                
    else:           # Альтернатвное решение без подбашен
        sw_alt = StopWatch()
        cost, path = solveGraph(diskCount,rodCost)

        print(cost, path)
        
        # один формат наш, другой Васекина, можно оставить любой или выпилить все для скорости
        sw_alt.stop()
        exportPath1 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path.txt".format(FILENAME.split('.')[0])))
        exportPath2 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path2.txt".format(FILENAME.split('.')[0])))
        solver.exportPathToFile(exportPath1, path, cost)
        # exportPathToFileAlternate(exportPath2, path, cost)

        print("Total cost: {0}".format(cost))
    #Вывод стоимости на каждом этапе
    print("- - - - - - - - - - - - - - - - - - - - - - -")
    print("Dst_rod = ",dst_rod)
    print("Stage cost")
    stageName = ['1 pyr 3','1 pyr 4','1 pyr 5','1 pyr 6','2 pyr 66','2 pyr 65','2 pyr 64','2 pyr 63','2 pyr 55','2 pyr 54','2 pyr 53','2 pyr 44',
                '2 pyr 43','2 pyr 33','1 pyr 7','2 pyr 77','2 pyr 76','2 pyr 75','2 pyr 74','2 pyr 73','1 pyr 8','2 pyr 88','2 pyr 87','2 pyr 86','2 pyr 85',
                '2 pyr 84','2 pyr 83','3 pyr 333','3 pyr 443','3 pyr 543','3 pyr 553','3 pyr 653','3 pyr 663','3 pyr 555','3 pyr 654']
    for i in range_maxStage:
        print("Stage ",stageName[i],":\t {0}".format(stageCost[i]))

    
def condition_check(diskCount,rodCost,dst_rod,stage):                          #выбор постоения пирамиды

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
        if diskCount > 14 and diskCount < 19:
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
    if stage == 14:
        if (diskCount > 8 and diskCount < 16) or len(rodCost)==4:
            cost,path_dst,path_end = pyramid_7(rodCost,dst_rod)
            rodCost.pop(dst_rod)
            diskCount-=7
            return cost,path_dst,path_end,diskCount
        else:
            print('STAGE 14: ERR count disk')
    if stage == 15:
        if diskCount > 16:
           return pyramid_xx(diskCount,rodCost,dst_rod,7,7)
        else:
            print('STAGE 15: ERR count disk')
    if stage == 16:
        if diskCount > 15:
           return pyramid_xx(diskCount,rodCost,dst_rod,7,6)
        else:
            print('STAGE 16: ERR count disk')
    if stage == 17:
        if diskCount > 15:
           return pyramid_xx(diskCount,rodCost,dst_rod,7,5)
        else:
            print('STAGE 16: ERR count disk')
    if stage == 18:
        if diskCount > 14 and diskCount < 18:
           return pyramid_xx(diskCount,rodCost,dst_rod,7,4)
        else:
            print('STAGE 18: ERR count disk')
    if stage == 19:
        if diskCount > 13 and diskCount < 17:
           return pyramid_xx(diskCount,rodCost,dst_rod,7,3)
        else:
            print('STAGE 19: ERR count disk')
    if stage == 20:
        if diskCount > 12 and diskCount < 18:
            return pyramid_xxx(diskCount,rodCost,dst_rod,3,3,3)
    else:
        print('STAGE 20: ERR count disk')
    if stage == 21:
        if diskCount > 13:
            return pyramid_xxx(diskCount,rodCost,dst_rod,4,4,3)
    else:
        print('STAGE 21: ERR count disk')
    if stage == 22:
        if diskCount > 14:
            return pyramid_xxx(diskCount,rodCost,dst_rod,5,4,3)
    else:
        print('STAGE 22: ERR count disk')
    if stage == 23:
        if diskCount > 15:
            return pyramid_xxx(diskCount,rodCost,dst_rod,5,5,3)
    else:
        print('STAGE 23: ERR count disk')
    if stage == 24:
        if diskCount > 16:
            return pyramid_xxx(diskCount,rodCost,dst_rod,6,5,3)
    else:
        print('STAGE 25: ERR count disk')
    if stage == 25:
        if diskCount > 17:
            return pyramid_xxx(diskCount,rodCost,dst_rod,6,6,3)
    else:
        print('STAGE 25: ERR count disk')
    if stage == 26:
        if diskCount > 17:
            return pyramid_xxx(diskCount,rodCost,dst_rod,5,5,5)
    else:
        print('STAGE 26: ERR count disk')
    if stage == 27:
        if diskCount > 17:
            return pyramid_xxx(diskCount,rodCost,dst_rod,6,5,4)
    else:
        print('STAGE 27: ERR count disk')



    #!Делаем это в конце так как подбашни могу уменьшить число дисков так, что станет меньше, чем штырей
    while len(rodCost)>diskCount:                                # Убираем самые дорогие штыри пока количество штыре не будет равно или меньше дисков
        rodCost.pop()

    cost = 0
    path_dst = []
    path_end = []
    return cost,path_dst,path_end,diskCount









if __name__ == "__main__": 
    FOLDERNAME = "solver_test/"
    FILENAME = "8d6r.txt" 
    

    dst_rod = 3
    stage_param = 4

    if len(sys.argv) < 2:
        print("WARN! Use predefined value!")   
    elif len(sys.argv) < 4:
        if "hanoi_graph.py" in str(sys.argv[1]):
            print("WARN! Detect VS Code, use predefined value!")
        else:
            FILENAME = str(sys.argv[1])
            dst_rod = int(sys.argv[2])
    elif len(sys.argv) < 3:
        if "hanoi_graph.py" in str(sys.argv[1]):
            print("WARN! Detect VS Code, use predefined value!")
        else:
            FILENAME = str(sys.argv[1])
    else:
        if "hanoi_graph.py" in str(sys.argv[1]):
            print("WARN! Detect VS Code, use predefined value!")
        else:
            FILENAME = str(sys.argv[1])
            dst_rod = int(sys.argv[2])
            stage_param = int(sys.argv[3])

    FILEPATH = FOLDERNAME + FILENAME
    import InputTXT as par
    parser = par.InputTXT()

    diskCount, column, diskCost, err = parser.ReadDisk(FILEPATH)
    print('TESTFILE: %s' % (FILEPATH))
    print(' DiskCount = ',diskCount,'\n','Column = ', column,'\n','Err = ', err,'\n', 'Cost', diskCost)

    # order, sizeOrder, returnErr = parser.ReadOrder(FILENAME)
    if err == 'OK':
        sw = StopWatch()
        hanoi_gr_pre(diskCount, diskCost,dst_rod,stage_param)
        sw.stop()

        

