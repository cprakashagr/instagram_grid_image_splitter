import cv2
import sys
import os

def main():

    totalI = int(sys.argv[1])
    totalJ = int(sys.argv[2])
    inImage = sys.argv[3]

    image = cv2.imread(inImage)
    split = 700

    f = totalI * totalJ - 1
    folderName = os.path.dirname(inImage)

    startX = 0
    startY = 0

    for j in range(0, totalJ):
        for i in reversed(range(0, totalI)):
            startX = i*split
            startY = j*split
            endX   = startX + split
            endY   = startY + split

            img = image[startY:endY, startX:endX]

            newFile = os.path.join(folderName, "{}.png".format(f))
            cv2.imwrite(newFile, img)
            f = f-1


if __name__ == "__main__":
    print ("Usages: python makeGrid.py xAxis(columns) yAxis(rows) inputImage")
    print ("Assumption: The input image is already in square format. Preferrably - 700x multiplier pixels.")
    print ("Not intending to maintain it any further - this was done for completely personal use. :) ")
    main()

