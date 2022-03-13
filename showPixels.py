import time
import matplotlib.pyplot as plt
from random import sample
from Node import Node
from ConvertPicture import ConvertPicture


def createPixels(numberOfPixels: int):
    pixels = []
    index = 0
    for y in range(numberOfPixels):
        for x in range(numberOfPixels):
            pixels.append(Node(index, x, -y, 0))
            index += 1

    # Naighbors
    for i in range(numberOfPixels * (numberOfPixels - 1)):
        pixels[i].neighbor_nodes.append(pixels[i + 1])
        pixels[i].neighbor_nodes.append(pixels[i + numberOfPixels])

    for i in range(
        numberOfPixels * (numberOfPixels - 1), numberOfPixels * numberOfPixels - 1
    ):
        pixels[i].neighbor_nodes.append(pixels[i + 1])

    index = 0
    for node in pixels:

        sameNode = pixels.pop(index)

        for selectedNode in sample(pixels, 6):
            node.neighbor_nodes.append(selectedNode)

        pixels.insert(index, sameNode)
        index += 1

    return pixels


def DFS(pixel: Node, imageDictionry: dict, pixels):

    plt.ion()

    figure, ax = plt.subplots(figsize=(10, 8))
    for point in pixels:
        ax.plot(point.X, point.Y, "o", color=pixel.color)

    plt.title("Your picture", fontsize=20)

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    visited = []
    stack = [pixel]

    while len(stack):
        pixel = stack.pop()

        if pixel not in visited:
            pixel.color = imageDictionry[pixel.Id]
            imageDictionry.pop(pixel.Id)
            visited.append(pixel)

            ax.plot(pixel.X, pixel.Y, "o", color=pixel.color)
            figure.canvas.draw()
            figure.canvas.flush_events()
            time.sleep(0.1)

        for node in pixel.neighbor_nodes:
            if node not in visited:
                stack.append(node)


def BFS(pixel: Node, imageDictionry: dict, pixels):

    plt.ion()

    figure, ax = plt.subplots(figsize=(10, 8))
    for point in pixels:
        ax.plot(point.X, point.Y, "o", color=pixel.color)

    plt.title("Your picture", fontsize=20)

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    visited = [pixel]
    queue = [pixel]

    while queue:
        pixel = queue.pop(0)

        pixel.color = imageDictionry[pixel.Id]
        imageDictionry.pop(pixel.Id)

        ax.plot(pixel.X, pixel.Y, "o", color=pixel.color)
        figure.canvas.draw()
        figure.canvas.flush_events()
        time.sleep(0.1)

        for node in pixel.neighbor_nodes:
            if node not in visited:
                queue.append(node)
                visited.append(node)


if __name__ == "__main__":
    startTime = time.time()
    picture = ConvertPicture("./img/pic-16.jpg")
    imageDict = picture.toDictionry()
    pixels = createPixels(16)
    # DFS(pixels[0], imageDict, pixels)
    BFS(pixels[0], imageDict, pixels)
    elapsedTime = time.time() - startTime
    print(elapsedTime)

    # for pixel in pixels:
    #     plt.plot(pixel.X, pixel.Y, "o", color=pixel.color)

    # plt.title("Your picture")
    # plt.show()
