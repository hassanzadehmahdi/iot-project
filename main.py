from random import randrange, sample
from Draw import Draw
from Node import Node
from SearchAlgorithm import SearchAlgorithm

#######################################################################################
def createListOfNodes(numberOfNodes: int):
    listOfNodes = []
    for i in range(numberOfNodes):
        listOfNodes.append(
            Node(i, randrange(0, 100), randrange(0, 100), randrange(0, 100))
        )
    return listOfNodes


#######################################################################################
def randomNeighbor(listOfNodes: list, numberOfNeighbors: int):
    index = 0
    for node in listOfNodes:

        sameNode = listOfNodes.pop(index)

        for selectedNode in sample(listOfNodes, numberOfNeighbors):
            node.neighbor_nodes.append(selectedNode)

        listOfNodes.insert(index, sameNode)
        index += 1


#######################################################################################
if __name__ == "__main__":

    numberOfNodes = int(input("Please, enter the number of nodes that you want: "))
    numberOfNeighbors = int(
        input("Please, enter the number of neighbors that you want: ")
    )
    firstNode = int(input("Please, enter the first node number that you want: "))
    secondNode = int(input("Please, enter the second node number that you want: "))

    listOfNodes = createListOfNodes(numberOfNodes)
    randomNeighbor(listOfNodes, numberOfNeighbors)
    searchAlgorithm = SearchAlgorithm()
    draw = Draw()

    paths = searchAlgorithm.DFS(listOfNodes[firstNode], listOfNodes[secondNode])

    directPath = []
    indirectPaths = []
    shortestPath = []

    for path in paths:
        if len(path) == 2:
            directPath = path
        else:
            indirectPaths.append([len(path), path])

    indirectPaths.sort(key=lambda x: x[0])

    if directPath:
        shortestPath = directPath
    elif indirectPaths:
        shortestPath = indirectPaths[0]
    

    print("Direct path: {}".format(directPath))
    print("One of indirect paths: {}".format(indirectPaths[0]))
    print("Number of Paths: {}".format(len(paths)))
    print("Shortest paths: {}".format(shortestPath))

    draw.showPlot(listOfNodes)
    draw.showPlot3D(listOfNodes)

    for path in paths:
        draw.showPath(listOfNodes, path)
