import os
import sys

import networkx as nx
import matplotlib.pyplot as plt 


class HanoiGraph():
    ''' класс графа с проверкой ограничений при добавлении вершин;
        считается, что башня построена на 0-ом штыре;       
        положение дисков представлено списком;
        первый элемент - нулевой (наименьший диск)
    '''
    PRINT_PREFIX = '[HGRAPH]: '
    ROOT_NODE_COLOR = '#b41f1f'
    ORDINARY_NODE_COLOR = '#1f78b4'
    
    # входные аргументы: кол-во дисков и список со стоимостью каждого штыря
    def __init__(self, diskCount, rodCostList):
        self.graph = nx.DiGraph() # представим положение дисков как вершину направленного графа

        self.diskCount = diskCount
        self.rodCount = len(rodCostList)
        
        root = str("0" * diskCount) # используем строку потому что надо хешируемый контейнер                    
        self.graph.add_node(root, color=self.ROOT_NODE_COLOR) # "корень" = начальное состояние

        self.graph.add_node("100", color=self.ORDINARY_NODE_COLOR)
        # TODO: условия добавляемости нод и способ добавления, проверить на примере

    # если есть диск с меньшим индексом на том же кольце -> текущий диск заблокирован
    def isDiskLocked(self, currentNode, diskIndex):
        result = False
        for i in range(0, diskIndex):
            if currentNode[i] == currentNode[diskIndex]:
                result = True
        return result
            
    # если на стержне для переноса есть с диск с меньшим индексом -> текущий диск перенести нельзя 
    def isDiskMoveLocked(self, currentNode, dstNode, diskIndex):
        result = False
        for i in range(0, self.diskIndex):
            if dstNode[i] == currentNode[diskIndex]:
                result = True
        return result

    # возращает список цветов нод
    def getNodeColors(self):
        colors = [] 
        return '#b41f1f' # TODO

    def draw(self):
        plt.figure(figsize=(8,8))
        nx.draw(self.graph, with_labels=True, font_weight='bold', node_color=self.getNodeColors())

        plt.show() 

if __name__ == "__main__":  
    graph = HanoiGraph(3, [1, 2, 3])

    graph.draw()