from random import randint, randrange, sample
from Node import Node

#######################################################################################
def createNodes(numberOfNodes: int):
    listOfNodes = []
    for index in range(numberOfNodes):
        node = Node(index, randrange(0, 100), randrange(0, 100), randrange(0, 100))
        node.dvr_table[index] = (0, index)
        listOfNodes.append(node)
    return listOfNodes


#######################################################################################
def createRandomNeighbor(listOfNodes: list, numberOfNeighbors: int):
    index = 0
    for node in listOfNodes:

        sameNode = listOfNodes.pop(index)

        for selectedNode in sample(listOfNodes, numberOfNeighbors):
            if selectedNode not in node.neighbor_nodes:

                node.neighbor_nodes.append(selectedNode)
                selectedNode.neighbor_nodes.append(node)

                cost = randint(1, 20)
                node.dvr_table[selectedNode.Id] = (cost, selectedNode.Id)
                selectedNode.dvr_table[node.Id] = (cost, node.Id)

        listOfNodes.insert(index, sameNode)
        index += 1


#######################################################################################
def DVR(node: Node):
    for neighbor in node.neighbor_nodes:
        for key in neighbor.dvr_table.keys():
            if key not in node.dvr_table.keys():
                node.dvr_table[key] = (
                    node.dvr_table[neighbor.Id][0] + neighbor.dvr_table[key][0],
                    neighbor.Id,
                )
            else:
                newCost = node.dvr_table[neighbor.Id][0] + neighbor.dvr_table[key][0]
                if newCost < node.dvr_table[key][0]:
                    node.dvr_table[key] = (
                        newCost,
                        neighbor.Id,
                    )


if __name__ == "__main__":
    # step 0
    listOfNodes = createNodes(5)

    # step 1
    createRandomNeighbor(listOfNodes, 2)

    for node in listOfNodes:
        print(node.Id, ": ", node.dvr_table)

    # step 2
    for _ in range(len(listOfNodes) - 2):
        for node in listOfNodes:
            DVR(node)

    print("=" * 70)

    for node in listOfNodes:
        print(node.Id, ": ", node.dvr_table)
