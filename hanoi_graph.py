import networkx as nx
import matplotlib.pyplot as plt 

# TODO: поправить проверки как у hanoi_graph_order
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
    # def isDiskMoveLocked(self, currentNode, dstNodeName, diskIndex):
    #     result = False
    #     for i in range(0, diskIndex):
    #         if dstNodeName[i] == currentNode["name"][diskIndex]:
    #             result = True
    #     return result
      # если на стержне для переноса есть с диск с меньшим индексом -> текущий диск перенести нельзя #FIXME: перенос большего на меньший
    def isDiskMoveLocked(self, dstNodeName, diskIndex):
        result = False
        for i in range(0, diskIndex):
            if dstNodeName[i] == dstNodeName[diskIndex]:
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
