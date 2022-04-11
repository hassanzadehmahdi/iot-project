class Node:
    def __init__(self, id: int, x: int, y: int, z: int) -> None:
        self.Id = id
        self.X = x
        self.Y = y
        self.Z = z
        self.neighbor_nodes = []
        self.dvr_table = {}
        self.color = "#fff"

    def __repr__(self) -> str:
        return "<Node {}>".format(self.Id)

    def __str__(self) -> str:
        return "Node {} with X: {}, Y: {}, Z: {} has {} neighbor".format(
            self.Id, self.X, self.Y, self.Z, len(self.neighbor_nodes)
        )

    def printNeighbors(self) -> str:
        for node in self.neighbor_nodes:
            print(node)
