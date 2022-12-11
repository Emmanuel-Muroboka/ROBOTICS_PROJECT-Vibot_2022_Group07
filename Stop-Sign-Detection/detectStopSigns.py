import imutils
import numpy as np



def meanSquareError(img1, img2):
    assert img1.shape == img2.shape, "Images must be the same shape."
    error = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
    error = error/float(img1.shape[0] * img1.shape[1] * img1.shape[2])
    return error

def compareImages(img1, img2):
    return 1/meanSquareError(img1, img2)


def pyramid(image, scale = 1.5, minSize = 30, maxSize = 1000):
    yield image
    while True:
        w = int(image.shape[1] / scale)
        image = imutils.resize(image, width = w)
        if(image.shape[0] < minSize or image.shape[1] < minSize):
            break
        if (image.shape[0] > maxSize or image.shape[1] > maxSize):
            continue
        yield image


def sliding_window(image, stepSize, windowSize):
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            yield (x, y, image[y:y+windowSize[1], x:x+windowSize[1]])

import argparse
import cv2
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the target image")
ap.add_argument("-p", "--prototype", required=True, help="Path to the prototype object")
args = vars(ap.parse_args())

targetImage = cv2.imread(args["image"])

targetImage = imutils.resize(targetImage, width=500)
prototypeImg = cv2.imread(args["prototype"])

maxSim = -1
maxBox = (0,0,0,0)

t0 = time.time()

for p in pyramid(prototypeImg, minSize = 50, maxSize = targetImage.shape[0]):
    for (x, y, window) in sliding_window(targetImage, stepSize = 2, windowSize = p.shape):
        if window.shape[0] != p.shape[0] or window.shape[1] != p.shape[1]:
            continue

        tempSim = compareImages(p, window)
        if(tempSim > maxSim):
            maxSim = tempSim
            maxBox = (x, y, p.shape[0], p.shape[1])

t1 = time.time()

print("Execution time: " + str(t1 - t0))
print(maxSim)
print(maxBox)
buff1 = 75
(x, y, w, h) = maxBox

cv2.rectangle(targetImage,(int(x-buff1/2),int(y-buff1/2)),(int(x+w+buff1/2),int(y+h+buff1/2)),(150,230,75),2)


cv2.imshow('image', targetImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
