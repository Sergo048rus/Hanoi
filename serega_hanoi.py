
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
    cost, path = solver.BuildPath(diskCountCurr,rodCost,0,1)
    return cost, path

def pyramid_3(rodCost,dst_rod):                # Собираем пирамиду из 3 дисков на одном штыре 
    cost_dst, path_dst = solver.BuildPath(3,rodCost,0,dst_rod)
    cost_end, path_end = solver.BuildPath(3, rodCost, dst_rod, 1)
    cost = cost_end+cost_dst
    return cost, path_dst,path_end


def pyramid_4(rodCost,dst_rod):                # Собираем пирамиду из 4 дисков на одном штыре
    cost_dst, path_dst = solver.BuildPath(4, rodCost, 0, dst_rod)
    cost_end, path_end = solver.BuildPath(4, rodCost, dst_rod, 1)
    cost = cost_end+cost_dst
    return cost, path_dst,path_end

def pyramid_5(rodCost,dst_rod):                # Собираем пирамиду из 3 дисков на одном штыре 
    cost_dst, path_dst = solver.BuildPath(5, rodCost, 0, dst_rod)
    cost_end, path_end = solver.BuildPath(5, rodCost, dst_rod, 1)
    cost = cost_end+cost_dst
    return cost, path_dst,path_end

def pyramid_6(rodCost,dst_rod):                # Собираем пирамиду из 4 дисков на одном штыре
    cost_dst, path_dst = solver.BuildPath(6, rodCost, 0, dst_rod)
    cost_end, path_end = solver.BuildPath(6, rodCost, dst_rod, 1)
    cost = cost_end+cost_dst
    return cost, path_dst,path_end


def hanoi_gr_pre(diskCount, rodCostList,dst_rod):
    
    rodCount = len(rodCostList)
    rodCost = rodCostList


    sort_rod(rodCost)

    print(rodCost)
    rodCost_sort = copy.deepcopy(rodCost)
    for stage in range(4):
        rodCost = copy.deepcopy(rodCost_sort)

        cost = 0
        path = []
        cost_pyro,path_dst,path_end,diskCountCurr = condition_check(diskCount,rodCost,dst_rod,stage)              # необходимо разобрться какие условия и сколько строить башен
        cost_graph, path_graph = solveGraph(diskCountCurr,rodCost)

        cost = cost_pyro + cost_graph
        path = path_dst+path_graph+path_end
        print(cost, path)
    
        # один формат наш, другой Васекина, можно оставить любой или выпилить все для скорости
        exportPath1 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path.txt".format(FILENAME.split('.')[0])))
        exportPath2 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path2.txt".format(FILENAME.split('.')[0])))
        solver.exportPathToFile(exportPath1, path, cost)
        # exportPathToFileAlternate(exportPath2, path, cost)

        # print("Shortest path: {0}".format(graph.orderPath))
        print("Total cost: {0}".format(cost))


        



    
def condition_check(diskCount,rodCost,dst_rod,stage):                          #выбор постоения пирамиды
    while len(rodCost)>diskCount:                                # Убираем самые дорогие штыри пока количество штыре не будет равно или меньше дисков
        rodCost.pop()
    if stage == 0:
        if diskCount > 3:
            cost,path_dst,path_end = pyramid_3(rodCost,dst_rod)
            rodCost.pop(dst_rod)
            diskCount-=3
            return cost,path_dst,path_end,diskCount
        else:
            print('STAGE 0: ERR count disk')
    if stage == 1:
        if diskCount > 4:
            cost,path_dst,path_end = pyramid_4(rodCost,dst_rod)
            rodCost.pop(dst_rod)
            diskCount-=4
            return cost,path_dst,path_end,diskCount
        else:
            print('STAGE 1: ERR count disk')
    if stage == 2:
        if diskCount > 5:
            cost,path_dst,path_end = pyramid_5(rodCost,dst_rod)
            rodCost.pop(dst_rod)
            diskCount-=5
            return cost,path_dst,path_end,diskCount
        else:
            print('STAGE 2: ERR count disk')
    if stage == 3:
        if diskCount > 6:
            cost,path_dst,path_end = pyramid_6(rodCost,dst_rod)
            rodCost.pop(dst_rod)
            diskCount-=6
            return cost,path_dst,path_end,diskCount
        else:
            print('STAGE 3: ERR count disk')






if __name__ == "__main__": 
    FOLDERNAME = "solver_test/"
    FILENAME = "8d6r.txt" 
    FILEPATH = FOLDERNAME + FILENAME

    dst_rod = 3

    if len(sys.argv) < 3:
        print("WARN! Use predefined value!")   
    else:
        if "hanoi_graph.py" in str(sys.argv[1]):
            print("WARN! Detect VS Code, use predefined value!")
        else:
            FILENAME = str(sys.argv[1])
            dst_rod = str(sys.argv[2])



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

        

