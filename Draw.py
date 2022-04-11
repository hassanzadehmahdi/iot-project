from random import choice
import matplotlib.pyplot as plt
import Annotation3D
import Arrow3D


class Draw:
    def __init__(self):
        pass

    def showPlot(self, listOfNodes: list):
        for node in listOfNodes:
            plt.plot(node.X, node.Y, "ro")
            plt.annotate(node.Id, (node.X + 1, node.Y - 0.5))
            arrowColor = "#" + "".join([choice("0123456789ABCDEF") for _ in range(6)])

            for neighbor in node.neighbor_nodes:
                plt.arrow(
                    node.X,
                    node.Y,
                    neighbor.X - node.X,
                    neighbor.Y - node.Y,
                    width=0.25,
                    length_includes_head=True,
                    head_width=3,
                    head_length=2,
                    color=arrowColor,
                )

        plt.title("2d plot")
        plt.show()

    def showPlot3D(self, listOfNodes: list):

        fig = plt.figure()
        ax = plt.axes(projection="3d")

        for node in listOfNodes:
            ax.plot(node.X, node.Y, node.Z, "ro")

            ax.annotate3D(
                node.Id,
                (node.X + 1, node.Y - 0.5, node.Z - 0.5),
                xytext=(3, 3),
                textcoords="offset points",
            )
            arrowColor = "#" + "".join([choice("0123456789ABCDEF") for _ in range(6)])

            for neighbor in node.neighbor_nodes:

                arrow_prop_dict = dict(
                    mutation_scale=20,
                    arrowstyle="-|>",
                    color=arrowColor,
                    shrinkA=0,
                    shrinkB=0,
                )

                ax.arrow3D(
                    node.X,
                    node.Y,
                    node.Z,
                    neighbor.X,
                    neighbor.Y,
                    neighbor.Z,
                    **arrow_prop_dict
                )

        ax.set_title("3d plot")
        plt.show()

    def showPath(self, listOfNodes: list, path: list):
        for node in listOfNodes:
            plt.plot(node.X, node.Y, "ro")
            plt.annotate(node.Id, (node.X + 1, node.Y - 0.5))

        arrowColor = "#" + "".join([choice("0123456789ABCDEF") for _ in range(6)])

        for i in range(len(path)):
            try:
                firstNode = path[i]
                secendNode = path[i + 1]

                plt.arrow(
                    firstNode.X,
                    firstNode.Y,
                    secendNode.X - firstNode.X,
                    secendNode.Y - firstNode.Y,
                    width=0.25,
                    length_includes_head=True,
                    head_width=3,
                    head_length=2,
                    color=arrowColor,
                )
            except:
                continue

        plt.title("2d plot")
        plt.show()
