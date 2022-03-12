import os
from PIL import Image
from datetime import datetime
from app.utils import *
from app.processImages import *
from config import *

def processImage(fileName):
    
    rawImage = Image.open(folderSource+"/"+fileName)
    rgbImage = rawImage.convert("RGB")
    hsvImage = rawImage.convert("HSV")

    rgbImagePx = rgbImage.load()
    hsvImagePx = hsvImage.load()

    rawImageSizeX = rawImage.size[0]
    rawImageSizeY = rawImage.size[1]
    rawImageSizeTotal = rawImageSizeX * rawImageSizeY

    startTime = datetime.now()
    print("        | Loaded " + fileName + " with " + str(rawImageSizeX) + "x" + str(rawImageSizeY) + " pixels (" + str(rawImageSizeTotal) + " total).")
    print("        | \n\n")

    for cursorX in range(rawImageSizeX):
        for cursorY in range(rawImageSizeY):
            printProcessingStatus(cursorX, cursorY, rawImageSizeY, rawImageSizeTotal, startTime)
            
            # RGB
            # rgbCurrentColor = rgbImagePx[cursorX, cursorY]
            # if rgbCurrentColor != rgbSubstituteColor:
            #     # check = recolorByThresholdMin(rgbImagePx[cursorX, cursorY], 80)
            #     check = recolorByThresholdRange(rgbCurrentColor, 0, 100)
            # else:
            #     check = False

            # if check:
            #     rgbImagePx[cursorX, cursorY] = rgbSubstituteColor

            # HSV
            hsvCurrentColor = hsvImagePx[cursorX, cursorY]
            if hsvCurrentColor != hsvSubstituteColor:
                check = recolorByHue(hsvCurrentColor)
            else: 
                check = False
            
            if check:
                hsvImagePx[cursorX, cursorY] = hsvSubstituteColor
    
    saveFile(rgbImage, hsvImage, fileName)

def processAllImages():
    files = os.listdir(folderSource)
    totalFiles = str(len(files))
    
    for i, file in enumerate(files):
        print("\n\nWORKING | IMAGE " + str(i+1) + " OF " + totalFiles)
        if file.endswith('.jpg') == False:
            print("        | ")
            print("ERROR   | Skipping " + file + " | please provide images in the jpg format")
        else:
            processImage( file )


