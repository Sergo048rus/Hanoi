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
    graph.add_node(root, weight=self.rodList[0], name=root) 

    genCounter = 0
    isEmpty = False
    while(isEmpty):
        isEmpty = makeGen(graph, src,dst)
        genCounter += 1
        print("mkGen #{0}".format(genCounter))
        
    print("Solved!")

def makeGen(graph, src, dst):


if __name__ == "__main__": 
    FILENAME = "10d3r.txt"

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
        cost, path = BuildPath(diskCount, diskCost, debugLevel=0)
        sw.stop()
        
        # exportPath = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_out.txt".format(FILENAME.split('.')[0])))
        # graph.exportGen(exportPath)
        # graph.draw()

        # sw = StopWatch()
        # calcCostBF(0,1) 
        # sw.stop()

        # один формат наш, другой Васекина, можно оставить любой или выпилить все для скорости
        exportPath1 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path.txt".format(FILENAME.split('.')[0])))
        exportPath2 = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_path2.txt".format(FILENAME.split('.')[0])))
        exportPathToFile(exportPath1, path, cost)
        # exportPathToFileAlternate(exportPath2, path, cost)

        # print("Shortest path: {0}".format(graph.orderPath))
        print("Total cost: {0}".format(cost))
