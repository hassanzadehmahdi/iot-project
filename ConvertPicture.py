from PIL import Image
from pylab import array


class ConvertPicture:
    def __init__(self, picturePath: str) -> None:
        self.picturePath = picturePath
        self.imageArray = array(Image.open(self.picturePath))

    def toDictionry(self):
        imageDict = {}
        index = 0
        for row in self.imageArray:
            for column in row:
                imageDict[index] = "#%02x%02x%02x" % (column[0], column[1], column[2])
                index += 1

        return imageDict

    def toFile(self, fileName: str):

        for row in self.imageArray:
            for column in row:

                f = open(fileName, "a")
                f.write("#%02x%02x%02x" % (column[0], column[1], column[2]) + " ")

        f.close()
