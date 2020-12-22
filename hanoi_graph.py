import os
import sys
import networkx as nx
import matplotlib.pyplot as plt 

from stopwatch import StopWatch

# ! ТЕКУЩАЯ ГЛАВНАЯ ПРОБЕЛМА - проверка всех предыдущих нод

class HanoiGraph():
    ''' класс графа с проверкой ограничений при добавлении вершин\n
        считается, что башня построена на 0-ом штыре\n      
        положение дисков представлено строкой\n
        первый элемент - нулевой (наименьший диск)
    '''
    PRINT_PREFIX = '[HGRAPH]: '
    DEBUG_LEVEL = 0 
    ROOT_NODE_COLOR = '#b41f1f'
    ORDINARY_NODE_COLOR = '#1f78b4'

    def DEBUG_PRINT(self, dstr):
        if self.DEBUG_LEVEL == 0: 
            print(self.PRINT_PREFIX + str(dstr)) 
 
    # входные аргументы: кол-во дисков и список со стоимостью каждого штыря
    def __init__(self, diskCount, rodCostList, debugLevel=1):
        self.DEBUG_LEVEL = debugLevel
        self.graph = nx.DiGraph() 

        self.diskCount = diskCount
        self.diskRange = range(0,diskCount)

        self.rodCount = len(rodCostList)
        self.rodCost = rodCostList
        self.rodRange = range(0,self.rodCount)

        self.orderCost = 0
        self.orderPath = []
        
        root = str("0" * diskCount) # используем строку, потому что надо хешируемый контейнер                    
        self.graph.add_node(root, color=self.ROOT_NODE_COLOR, # "корень" = начальное состояние
                                  weight=self.rodCost[0],
                                  name=root) 

        self.genIndex = 0
        self.genDict = {self.genIndex: [root]} # словарь со списком нод каждого "поколения" типа string
        self.placedDiskCount = 0               # количество вставших на место дисков

        while len(self.genDict[self.genIndex]) != 0: 
        # while self.genIndex < 5:  
            print(("Try makeGen #{i}".format(i=self.genIndex))) #! slow print 

            ngen = self.makeGen(self.genIndex, '1')
            self.genIndex += 1
            self.genDict[self.genIndex] = ngen
            print(len(ngen)) #! slow print
        
        self.DEBUG_PRINT("No turns on gen #{i}".format(i=self.genIndex))
        # self.printGen() #! slow print

    # пройтись по текущему поколению и построить всевозможные ноды (тупо полный перебор)
    def makeGen(self, genIndex, targetRode):
        newGen = [] # TODO: list is slow containter
        
        diskPlaced = False
        # для каждой ноды в текущем поколении
        for node in self.genDict[genIndex]:

            srcBlocked = False
            dstBlocked = False
            # для каждого диска в ноде берем все возможные/невозможные варианты
            for i in range(0,len(node) - self.placedDiskCount): # без уже поставленных на место дисков
                for j in range(0,i):
                    if node[j] == node[i]:
                        srcBlocked = True
                        break
                if srcBlocked:
                    srcBlocked = False
                    continue
        
                for r in self.rodRange:
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
                        # print(node + "->" + repl + " gen " + str(genIndex)) 

                        if dstBlocked:
                            dstBlocked = False
                            continue
                       

                        # если такая нода возможна, добавляем ее
                        res = True
                        for newNode in newGen: # дупликат из новых
                            if newNode == repl:
                                res = False
                        if res:        
                            #res = self.checkGenDict(genIndex, repl) # проверяем, что новая нода не из предыдущих поколений
                            if self.graph.has_node(repl):
                                res = False
                        if res:
                            res = self.tryToAddNode(self.graph.nodes[node], repl, i) # пробуем добавить
                        if res: 
                            newGen.append(repl) 
                            if repl[-1 - self.placedDiskCount] == targetRode and repl[-1 - self.placedDiskCount + 1] == targetRode:
                                # print(repl + ' = ' + targetRode)
                                diskPlaced = True
                                
        if diskPlaced:  
            # print('Disk SET #{0}'.format(self.placedDiskCount + 1))
            self.placedDiskCount += 1
            # раз диск поставлен надо удалить остальные "неправильные" ноды
            newGen = [x for x in newGen if str(targetRode * self.placedDiskCount) in x[-1 - self.placedDiskCount + 1:]] 

        return newGen

    # возвращает True, если нет такой же ноды в предыдущих поколении
    def checkGenDict(self, genIndex, newNode):
        for i in range(0,genIndex+1):          # все 
        # for i in range(genIndex,genIndex+1): # предыдущие и текущее
            for node in self.genDict[i]:
                if node == newNode:
                    # self.DEBUG_PRINT("Gen duplicate {0}->{1}".format(node,newNode))
                    return False
        return True

    # вывод словаря поколений по поколениям в консоль
    def printGen(self):
        for k in self.genDict.keys():
            self.DEBUG_PRINT("gen #{0}: {1}".format(k,self.genDict[k]))

    # вывод словаря поколений по поколениям в файл
    def exportGen(self, filename):
        with open(str(filename), "w", encoding="utf-8") as fos:
            fos.write("=== Hanoi exportGen ===\r\n")
            for k in self.genDict.keys():
                fos.write("gen #{0}: {1}\r\n".format(k,self.genDict[k]))

    # добавляет ноду со связью, если это возможно
    def tryToAddNode(self, rootNode, dstNodeName, index):
        # countOfChanges = 0
        # changedIndex = 0
        # for i in range(0, self.diskCount):
        #     if rootNode["name"][i] != dstNodeName[i]:
        #         changedIndex = i
        #         countOfChanges += 1

        # if countOfChanges > 1:
        #     # self.DEBUG_PRINT("Multiple move [{dst}] <- [{root}]".format(i=changedIndex, dst=dstNodeName, root=rootNode["name"]))
        #     return False

        # if self.isDiskLocked(rootNode, changedIndex):
        #     # self.DEBUG_PRINT("Disk #{i} locked [{dst}] <- [{root}]".format(i=changedIndex, dst=dstNodeName, root=rootNode["name"]))
        #     return False

        # if self.isDiskMoveLocked(dstNodeName, changedIndex):
        #     # self.DEBUG_PRINT("Disk move locked [{dst}] <- [{root}]".format(i=changedIndex, dst=dstNodeName, root=rootNode["name"]))
        #     return False

        # for n in self.genDict[self.genIndex]:
        #     if self.graph.nodes[n]["name"] == dstNodeName:
        #         self.DEBUG_PRINT("Node [{0}] exists, add edge".format(dstNodeName))
        #         self.graph.add_edge(rootNode, n, weight=self.rodCost[int(dstNodeName[changedIndex])])
        #         return False

        self.graph.add_node(dstNodeName, color=self.ORDINARY_NODE_COLOR, # create node int(index)
                                         weight=self.rodCost[int(dstNodeName[index])],
                                         name=dstNodeName) 

        self.graph.add_edge(rootNode["name"], dstNodeName, weight=self.rodCost[int(dstNodeName[index])])
        
        # self.DEBUG_PRINT("Add node [{dst}] <-{cost}-- [{root}]".format(cost=self.rodCost[int(dstNodeName[changedIndex])],
        #                                                         dst=dstNodeName, root=rootNode["name"]))
        return True

    # если есть диск с меньшим индексом на том же кольце -> текущий диск заблокирован
    def isDiskLocked(self, currentNode, diskIndex):
        result = False
        for i in range(0, diskIndex):
            if currentNode["name"][i] == currentNode["name"][diskIndex]:
                result = True
        return result
            
    # если на стержне для переноса есть с диск с меньшим индексом -> текущий диск перенести нельзя 
    def isDiskMoveLocked(self, dstNodeName, diskIndex):
        result = False
        for i in range(0, diskIndex):
            if dstNodeName[i] == dstNodeName[diskIndex]:
                result = True
        return result

    # возращает список цветов нод #! DEPRECATED
    def getNodeColors(self):
        colors = [] 
        for n,d in self.graph.nodes(data=True):
            colors.append(d["color"])
        return colors

    def layoutNodes(self): # positions for all nodes 
        # return nx.spring_layout(self.graph)
        # return nx.bipartite_layout(self.graph, self.graph.nodes)
        # return nx.circular_layout(self.graph)
        # return nx.kamada_kawai_layout(self.graph)
        # return nx.planar_layout(self.graph)
        return nx.shell_layout(self.graph)
        # return nx.spectral_layout(self.graph)
           
    def draw(self):
        plt.figure(figsize=(7,7))
        pos = self.layoutNodes()
        nx.draw_networkx_nodes(self.graph, pos)                 # nodes [node_size=700]
        nx.draw_networkx_labels(self.graph, pos)

        labels = nx.get_edge_attributes(self.graph, 'weight')   # edge labels
        nx.draw_networkx_edges(self.graph, pos)
        nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=labels)
        
        # plt.axis("off")
        plt.show() 

    def calcCostDeijkstra(self, src, dst):
        self.DEBUG_PRINT("Start pathfinder - Deijkstra")
        srcNode = str(src) * self.diskCount
        dstNode = str(dst) * self.diskCount
        self.DEBUG_PRINT(srcNode + "-D>" + dstNode)
        self.orderCost, self.orderPath = nx.single_source_dijkstra(self.graph, srcNode, dstNode)


if __name__ == "__main__": 
    FILENAME = "10d5r.txt"

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
        graph = HanoiGraph(diskCount, diskCost, debugLevel=0)
        sw.stop()
        
        exportPath = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + ("/solver_out/{0}_out.txt".format(FILENAME.split('.')[0])))
        graph.exportGen(exportPath)
        # graph.draw()

        graph.calcCostDeijkstra(0,1) 
        print("Shortest path: {0}".format(graph.orderPath))
        print("Total cost: {0}".format(graph.orderCost))

