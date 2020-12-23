import os
import sys
import networkx as nx
import matplotlib.pyplot as plt 

from stopwatch import StopWatch

'''
Импортируется только эта функция: 
* import hanoi_graph_mod as solver
* solver.BuildPath(...)
Строит граф от src(int) к dst(int) возвращает стоимость(int) и путь(list) 
Дополнительно передается количество дисков и список штырей(весов)
'''
def BuildPath(diskCount, rodList, src, dst):
    graph = nx.DiGraph() 
    root = str(str(src) * diskCount) # строка, потом хешируется
    graph.add_node(root, weight=rodList[0], name=root) 

    genCounter = 0
    isEmpty = False
    placedCount = 0
    prevGen = [root]

    while not isEmpty:
        prevGen, isEmpty, placedCount = makeGen(graph, prevGen, placedCount, src, dst, diskCount, rodList)
        genCounter += 1
        print("mkGen #{0} {1}".format(genCounter, len(prevGen)))

    print("Solved!")

    return calcCostBF(graph, src, dst, diskCount)


def makeGen(graph, prevGen, placedCount, src, dst, diskCount, rodList):
    newGen = [] # TODO: should be optimized and deleted
    rodRange = range(0,len(rodList))
    diskPlaced = False
        
    # для каждой ноды в текущем поколении
    for node in prevGen:
        srcBlocked = False
        dstBlocked = False

        # для каждого диска в ноде берем все возможные/невозможные варианты
        for i in range(0,len(node) - placedCount): # без уже поставленных на место дисков
            if i != 0:
                for j in range(0,i):
                    if node[j] == node[i]:
                        srcBlocked = True
                        break
                if srcBlocked:
                    srcBlocked = False
                    continue
        
            for r in rodRange:
                if r != int(node[i]):        # если возможна замена, меняем i-й элемент 
                    if i == (len(node) - 1): # !check boundary cases!
                        repl = node[:i] + str(r)
                        for k in range(0,i):
                            if node[k] == str(r):
                                dstBlocked = True
                                break
                    elif i == 0:
                        repl = str(r) + node[1:]
                    else:
                        repl = node[:i] + str(r) + node[i+1:] 
                        for k in range(0,i):
                            if node[k] == str(r):
                                dstBlocked = True
                                break
                     

                    if dstBlocked:
                        dstBlocked = False
                        continue
                       
                    # если такая нода есть - не добавляем
                    if graph.has_node(repl):
                        continue
                    
                    # иначе добавляем
                    # print(node + "->" + repl + " i: " + str(int(node[i])))
                    graph.add_node(repl, weight=rodList[r], name=repl) 
                    graph.add_edge(node, repl, weight=rodList[r])

                    newGen.append(repl) 
                    if repl[-1 - placedCount] == str(dst): #and repl[-1 - placedCount + 1] == str(dst): #! не понял блять
                        # print(repl + ' = ' + targetRode)
                        diskPlaced = True
                                
    if diskPlaced:  
        placedCount += 1
        # раз диск поставлен надо удалить остальные "неправильные" ноды
        newGen = [x for x in newGen if str(str(dst) * placedCount) in x[-1 - placedCount + 1:]] 
    
    if len(newGen) != 0:
        isEmpty = False
    else:
        isEmpty = True

    return newGen, isEmpty, placedCount


#############################################
# Pathfinders
#############################################
def calcCostDeijkstra(graph, src, dst, diskCount):
        print("Start pathfinder - Deijkstra")
        srcNode = str(src) * diskCount
        dstNode = str(dst) * diskCount
        print(srcNode + "-D>" + dstNode)
        return nx.single_source_dijkstra(graph, srcNode, dstNode)

def calcCostBF(graph, src, dst, diskCount):
        print("Start pathfinder - Bellman-Ford")
        srcNode = str(src) * diskCount
        dstNode = str(dst) * diskCount
        print(srcNode + "-D>" + dstNode)
        return nx.single_source_bellman_ford(graph, srcNode, dstNode)

#############################################
# Вывод в файл
#############################################
def exportPathToFile(filepath, path, cost):
    with open(str(filepath), "w", encoding="utf-8") as fos:
        fos.write("=== Hanoi pathfinder result ===\r\n")
        fos.write("Cost: {0}\r\n".format(cost))
        fos.write("Path:\r\n")
        for move in path:
            fos.write("{0}\n".format(move))

def exportPathToFileAlternate(filepath, path, cost):
    with open(str(filepath), "w", encoding="utf-8") as fos:
        fos.write("=== Hanoi pathfinder result ===\r\n")
        fos.write("Cost: {0}\r\n".format(cost))
        fos.write("Path:\r\n")
        for i in range(1,len(path)):
            disk,src,dst = "","",""
            for j in range(0,len(path[i])):
                if path[i][j] != path[i-1][j]:
                    disk = j
                    src = path[i-1][j]
                    dst = path[i][j]
                    break
            fos.write("{0} {1} {2}\n".format(disk, src, dst))


#############################################
# MAIN
#############################################
if __name__ == "__main__": 
    FILENAME = "6d7r.txt"

    if len(sys.argv) < 2:
        print("WARN! Use predefined value!")   
    else:
        if "hanoi_graph.py" in str(sys.argv[1]):
            print("WARN! Detect VS Code, use predefined value!")
        else:
            FILENAME = str(sys.argv[1])

    FOLDERNAME = "solver_test/"
    FILEPATH = FOLDERNAME + FILENAME

    import InputTXT as par
    parser = par.InputTXT()

    diskCount, column, diskCost, err = parser.ReadDisk(FILEPATH)
    print('TESTFILE: %s' % (FILEPATH))
    print(' DiskCount = ',diskCount,'\n','Column = ', column,'\n','Err = ', err,'\n', 'Cost', diskCost)
    # order, sizeOrder, returnErr = parser.ReadOrder(FILENAME)

    if err == 'OK':
        sw = StopWatch()
        cost, path = BuildPath(diskCount, diskCost, 0, 1)
        sw.stop()

        print(cost, path)
        # sys.exit(0)

        # exportPath = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_out.txt".format(FILENAME.split('.')[0])))
        # graph.exportGen(exportPath)
        # graph.draw()


        # один формат наш, другой Васекина, можно оставить любой или выпилить все для скорости
        exportPath1 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path.txt".format(FILENAME.split('.')[0])))
        exportPath2 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path2.txt".format(FILENAME.split('.')[0])))
        exportPathToFile(exportPath1, path, cost)
        # exportPathToFileAlternate(exportPath2, path, cost)

        # print("Shortest path: {0}".format(graph.orderPath))
        print("Total cost: {0}".format(cost))
