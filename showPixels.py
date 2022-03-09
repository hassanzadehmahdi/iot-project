import matplotlib.pyplot as plt
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
        pixels[i].neighbor_nodes.append(pixels[i + 16])

    for i in range(
        numberOfPixels * (numberOfPixels - 1), numberOfPixels * numberOfPixels - 1
    ):
        pixels[i].neighbor_nodes.append(pixels[i + 1])

    return pixels


def DFS(pixel: Node, imageDictionry: dict):

    visited = []
    stack = [pixel]

    while len(stack):
        pixel = stack.pop()

        if pixel not in visited:
            pixel.color = imageDictionry[pixel.Id]
            imageDictionry.pop(pixel.Id)
            visited.append(pixel)

        for node in pixel.neighbor_nodes:
            if node not in visited:
                stack.append(node)


if __name__ == "__main__":
    picture = ConvertPicture("./img/pic-16.jpg")
    imageDict = picture.toDictionry()
    pixels = createPixels(16)
    DFS(pixels[0], imageDict)

    for pixel in pixels:
        plt.plot(pixel.X, pixel.Y, "o", color=pixel.color)

    plt.title("Your picture")
    plt.show()
