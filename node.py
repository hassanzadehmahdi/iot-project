# mahdi hassanzadeh


class node:
    def __init__(self, id: int, x: int, y: int) -> None:
        self.Id = (id,)
        self.X = x
        self.Y = y
        self.neighbor_nodes = []

    def __repr__(self) -> str:
        return "<Node {}>".format(self.Id[0])

    def __str__(self) -> str:
        return "Node {} with X: {}, Y: {} has {} neighbor".format(
            self.Id[0], self.X, self.Y, len(self.neighbor_nodes)
        )

    def printNeighbors(self) -> str:
        for node in self.neighbor_nodes:
            print(node)
