from copy import deepcopy
from Node import Node


class SearchAlgorithm:
    def __init__(self):
        self.visited = []
        self.notPossibleNodes = []
        self.currentPath = []
        self.paths = []
        self.pathsNode = []

    def DFS(self, firstNode: Node, secondNode: Node):

        self.visited.append(firstNode)
        self.currentPath.append(firstNode)

        if firstNode == secondNode:
            self.paths.append(deepcopy(self.currentPath))

            for path in self.currentPath:
                if path not in self.pathsNode:
                    self.pathsNode.append(path)

        else:
            for neighbour in firstNode.neighbor_nodes:
                if (
                    neighbour not in self.visited
                    and neighbour not in self.notPossibleNodes
                ):
                    self.DFS(neighbour, secondNode)

        self.currentPath.pop()
        self.visited.remove(firstNode)
        if firstNode not in self.pathsNode:
            self.notPossibleNodes.append(firstNode)

        if len(self.visited) == 0:
            return self.paths
