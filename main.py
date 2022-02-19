# mahdi hassanzadeh

from random import choice, randrange, sample
from copy import deepcopy
import matplotlib.pyplot as plt
from node import node


def createListOfNodes(numberOfNodes: int):
    listOfNodes = []
    for i in range(numberOfNodes):
        listOfNodes.append(node(i, randrange(0, 100), randrange(0, 100)))
    return listOfNodes


def randomNeighbor(listOfNodes: list, numberOfNeighbors: int):
    index = 0
    for node in listOfNodes:

        copyListOfNodes = deepcopy(listOfNodes)
        copyListOfNodes.pop(index)

        for selectedNode in sample(copyListOfNodes, numberOfNeighbors):
            node.neighbor_nodes.append(selectedNode)

        index += 1


def showPlot(listOfNodes: list):
    for node in listOfNodes:
        plt.plot(node.X, node.Y, "ro")
        plt.annotate(node.Id[0], (node.X + 1, node.Y - 0.5))
        arrowColor = "#" + "".join([choice("0123456789ABCDEF") for _ in range(6)])

        for neighbor in node.neighbor_nodes:
            plt.arrow(
                node.X,
                node.Y,
                neighbor.X - node.X,
                neighbor.Y - node.Y,
                width=0.25,
                length_includes_head=True,
                head_width=1.5,
                head_length=1,
                color=arrowColor,
            )

    plt.show()


if __name__ == "__main__":
    listOfNodes = createListOfNodes(20)
    randomNeighbor(listOfNodes, 6)
    showPlot(listOfNodes)
