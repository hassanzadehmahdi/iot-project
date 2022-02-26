from copy import deepcopy
from Node import Node


class SearchAlgorithm:
    def __init__(self):
        self.visited = []
        self.currentPath = []
        self.simplePaths = []

    def DFS(self, firstNode: Node, secondNode: Node):

        self.visited.append(firstNode)
        self.currentPath.append(firstNode)

        if firstNode == secondNode:
            self.simplePaths.append(deepcopy(self.currentPath))

        else:
            for neighbour in firstNode.neighbor_nodes:
                if neighbour not in self.visited:
                    self.DFS(neighbour, secondNode)

        self.currentPath.pop()
        self.visited.remove(firstNode)

        if len(self.visited) == 0:
            return self.simplePaths
