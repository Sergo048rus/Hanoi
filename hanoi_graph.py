import os
import sys

import networkx as nx
import matplotlib.pyplot as plt 

import InputTXT as parser
# ПРИМЕРЫ:
# for n,d in self.graph.nodes(data=True):
#     print(n,d)
#G.add_edge(1, 2, weight=4.7 )

# TODO: условия добавляемости нод и способ добавления, проверить на примере
class HanoiGraph():
    ''' класс графа с проверкой ограничений при добавлении вершин;
        считается, что башня построена на 0-ом штыре;       
        положение дисков представлено строкой;
        первый элемент - нулевой (наименьший диск)
    '''
    PRINT_PREFIX = '[HGRAPH]: '
    DEBUG_LEVEL = 0 
    ROOT_NODE_COLOR = '#b41f1f'
    ORDINARY_NODE_COLOR = '#1f78b4'

    def DEBUG_PRINT(self, dstr):
        if self.DEBUG_LEVEL == 0: 
            print(self.PRINT_PREFIX + str(dstr)) # TODO: смотреть предков и если совпадает то не строить (обр путь)
    
    # входные аргументы: кол-во дисков и список со стоимостью каждого штыря
    def __init__(self, diskCount, rodCostList):
        self.graph = nx.DiGraph() # представим положение дисков как вершину направленного графа

        self.diskCount = diskCount
        self.diskRange = range(0,diskCount)

        self.rodCount = len(rodCostList)
        self.rodCost = rodCostList
        
        root = str("0" * diskCount) # используем строку, потому что надо хешируемый контейнер                    
        self.graph.add_node(root, color=self.ROOT_NODE_COLOR, # "корень" = начальное состояние
                                  weight=self.rodCost[0],
                                  name=root) 

        self.genIndex = 0
        self.genDict = {self.genIndex: [root]} # словарь со списком нод каждого "поколения"

        while len(self.genDict[self.genIndex]) != 0: 
            self.DEBUG_PRINT("Try makeGen #{i}".format(i=self.genIndex))

            ngen = self.makeGen()
            self.genIndex += 1
            self.genDict[self.genIndex] = ngen
        
        self.DEBUG_PRINT("No turns on gen #{i}".format(i=self.genIndex))
        self.tryToAddNode(self.graph.nodes["000"],"100")
        self.tryToAddNode(self.graph.nodes["100"], "000")
        self.tryToAddNode(self.graph.nodes["000"], "120")
        self.tryToAddNode(self.graph.nodes["000"], "020")

    def makeGen(self):
        return []

    # добавляет ноду со связью, если это возможно
    def tryToAddNode(self, rootNode, dstNodeName):
        countOfChanges = 0
        changedIndex = 0
        for i in range(0, self.diskCount):
            if rootNode["name"][i] != dstNodeName[i]:
                changedIndex = i
                countOfChanges += 1

        if countOfChanges > 1:
            self.DEBUG_PRINT("Multiple move [{dst}] <- [{root}]".format(i=changedIndex, dst=dstNodeName, root=rootNode["name"]))
            return

        if self.isDiskLocked(rootNode, changedIndex):
            self.DEBUG_PRINT("Disk #{i} locked [{dst}] <- [{root}]".format(i=changedIndex, dst=dstNodeName, root=rootNode["name"]))
            return

        if self.isDiskMoveLocked(rootNode, dstNodeName, changedIndex):
            self.DEBUG_PRINT("Disk move locked [{dst}] <- [{root}]".format(i=changedIndex, dst=dstNodeName, root=rootNode["name"]))
            return

        for n in self.genDict[self.genIndex]:
            if self.graph.nodes[n]["name"] == dstNodeName:
                self.DEBUG_PRINT("Node [{0}] exists, add edge".format(dstNodeName))
                self.graph.add_edge(rootNode, n, weight=self.rodCost[int(dstNodeName[changedIndex])])
                return

        self.graph.add_node(dstNodeName, color=self.ORDINARY_NODE_COLOR, # create node
                                         weight=self.rodCost[int(dstNodeName[changedIndex])],
                                         name=dstNodeName) 

        self.graph.add_edge(rootNode["name"], dstNodeName, weight=self.rodCost[int(dstNodeName[changedIndex])])
        
        self.DEBUG_PRINT("Add node [{dst}] <-{cost}-- [{root}]".format(cost=self.rodCost[int(dstNodeName[changedIndex])],
                                                                dst=dstNodeName, root=rootNode["name"]))
        

    # если есть диск с меньшим индексом на том же кольце -> текущий диск заблокирован
    def isDiskLocked(self, currentNode, diskIndex):
        result = False
        for i in range(0, diskIndex):
            if currentNode["name"][i] == currentNode["name"][diskIndex]:
                result = True
        return result
            
    # если на стержне для переноса есть с диск с меньшим индексом -> текущий диск перенести нельзя 
    def isDiskMoveLocked(self, currentNode, dstNodeName, diskIndex):
        result = False
        for i in range(0, diskIndex):
            if dstNodeName[i] == currentNode["name"][diskIndex]:
                result = True
        return result

    # возращает список цветов нод
    def getNodeColors(self):
        colors = [] 
        for n,d in self.graph.nodes(data=True):
            colors.append(d["color"])
        return colors

    def draw(self):
        plt.figure(figsize=(8,8))
        nx.draw(self.graph, with_labels=True, node_color=self.getNodeColors()) 
        # TODO: отрисовка весов и pos'ов
        # pos = nx.get_node_attributes(self.graph,'pos')
        # labels = nx.get_edge_attributes(self.graph,'weight')
        # nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        plt.show() 


class HanoiGraphOrder():
    ''' аналог HanoiGraph, но стороит существующий ORDER
        реализованы все проверки кроме специфичных для HanoiGraph
        moveOrder = { "dI" : 0, "rSrc" : 0, "rDst" : 1 }
    '''
    PRINT_PREFIX = '[OGRAPH]: '
    DEBUG_LEVEL = 0 
    ROOT_NODE_COLOR = '#b41f1f'
    ORDINARY_NODE_COLOR = '#1f78b4'

    def __init__(self, diskCount, rodCostList, moveOrderList):
        self.graph = nx.DiGraph() 
        self.graph.add_node(str("0" * diskCount), color=self.ROOT_NODE_COLOR, # "корень" = начальное состояние
                                                weight=rodCostList[0],
                                                name=str("0" * diskCount))

        self.diskCount = diskCount
        self.diskRange = range(0,diskCount)
        self.rodRange = range(0, len(rodCostList))
        self.rodCount = len(rodCostList)
        self.rodCost = rodCostList

        self.plotMoveOrder(moveOrderList)

    # 1. нет такого диска +
    # 2. нет такого штыря +
    # 3. штыри совпадают  +
    # 4. дублирующийся ход
    # остальные проверки как у HanoiGraph
    def plotMoveOrder(self, moveOrderList):
        i = 0
        prevNodeName = str("0" * self.diskCount)

        for move in moveOrderList:
            print(self.PRINT_PREFIX + "Move {0} = {1}".format(i,move))
            i += 1

            if move["dI"] > self.diskCount or move["dI"] < 0:
                print(self.PRINT_PREFIX + "Invalid disk number #{i}".format(i=move["dI"]))
                return 

            if not move["rSrc"] in self.rodRange:
                print(self.PRINT_PREFIX + "Invalid src rod number #{i}".format(i=move["rSrc"]))
                return

            if not move["rDst"] in self.rodRange:
                print(self.PRINT_PREFIX + "Invalid dst rod number #{i}".format(i=move["rDst"]))
                return

            if move["rSrc"] == move["rDst"]:
                print(self.PRINT_PREFIX + "Duplicate {0} {1} {2}".format(move["dI"], move["rSrc"], move["rDst"]))
                return

            # формируем название ноды, где dI - индекс в строке, rSrc - тек. значение, rDst - новое значение
            # проверяем, что есть такая нода, где в dI есть rSrc
            dstNodeName = prevNodeName
            if dstNodeName[move["dI"]] != str(move["rSrc"]):
                invalid_node = dstNodeName[:move["dI"]] + str(move["rSrc"]) + dstNodeName[move["dI"]+1:]
                print(self.PRINT_PREFIX + "Node [{0}] does not exist!".format(invalid_node))
                return

            # с названием ноды все ОК, пытаемся добавиться
            dstNodeName = dstNodeName[:move["dI"]] + str(move["rDst"]) + dstNodeName[move["dI"]+1:]


            if self.isDiskLocked(self.graph.nodes[prevNodeName], move["dI"]):
                print(self.PRINT_PREFIX + "Disk locked {0}".format(move))
                return

            if self.isDiskMoveLocked(dstNodeName, move["dI"]):
                print(self.PRINT_PREFIX + "Disk move lock {0}".format(move))
                return

            self.graph.add_node(dstNodeName,    color=self.ORDINARY_NODE_COLOR, 
                                                weight=self.rodCost[move["rDst"]],
                                                name=dstNodeName)

            self.graph.add_edge(prevNodeName, dstNodeName, weight=self.rodCost[move["rDst"]])

            prevNodeName = dstNodeName

    # если есть диск с меньшим индексом на том же кольце -> текущий диск заблокирован
    def isDiskLocked(self, currentNode, diskIndex):
        result = False
        for i in range(0, diskIndex):
            if currentNode["name"][i] == currentNode["name"][diskIndex]:
                result = True
        return result
            
    # если на стержне для переноса есть с диск с меньшим индексом -> текущий диск перенести нельзя #FIXME: перенос большего на меньший
    def isDiskMoveLocked(self, dstNodeName, diskIndex):
        result = False
        for i in range(0, diskIndex):
            if dstNodeName[i] == dstNodeName[diskIndex]:
                result = True
        return result
            

    def draw(self):
        plt.figure(figsize=(8,8))
        nx.draw(self.graph, with_labels=True) 
        plt.show() 



#FIXME: пофиксить ошибку OGRAPH в основном графе
if __name__ == "__main__": 
    FILENAME = "tests_file/t3-1.txt" 
    parser = parser.InputTXT()

    diskCount, column, diskCost, err = parser.ReadDisk(FILENAME)
    print(' DiskCount = ',diskCount,'\n','Column = ', column,'\n','Err = ', err,'\n', 'Cost', diskCost)

    order, sizeOrder, returnErr = parser.ReadOrder(FILENAME)
    if returnErr == 0 and err == 0:
        graph = HanoiGraphOrder(diskCount, diskCost, order)
        graph.draw()


# moveTest1 = [{ "dI" : 0, "rSrc" : 0, "rDst" : 1 },
#          { "dI" : 1, "rSrc" : 0, "rDst" : 2 },
#          { "dI" : 0, "rSrc" : 1, "rDst" : 2 },
#          { "dI" : 2, "rSrc" : 0, "rDst" : 1 },
#          { "dI" : 0, "rSrc" : 2, "rDst" : 0 },
#          { "dI" : 1, "rSrc" : 2, "rDst" : 1 },
#          { "dI" : 0, "rSrc" : 0, "rDst" : 1 }
# ]

# G=nx.Graph()
# i=1
# G.add_node(i,pos=(i,i))
# G.add_node(2,pos=(2,2))
# G.add_node(3,pos=(1,0))
# G.add_edge(1,2,weight=0.5)
# G.add_edge(1,3,weight=9.8)
# pos=nx.get_node_attributes(G,'pos')
# nx.draw(G,pos,with_labels=True)
# labels = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
# plt.show() 