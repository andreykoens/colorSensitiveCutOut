import os
from datetime import datetime
from config import *

def printProcessingStatus(X, Y, sizeY, total, startTime):
    current = ((X * sizeY) + Y) + 1
    percentage = round((current/total)*100, 0)
    currentTime = datetime.now() - startTime
    if currentTime.microseconds % 100000 == 0 or current == total:
        print("\033[F", end="")
        print("\033[F", end="")
        
        bar = ""
        for i in range(50):
            if i > (percentage/2):
                bar += "░"
            else:
                bar += "▓"
    
        print("        | ▓ " + str(percentage) + "% " + bar + " |", end="          \n")
        print("        | Analyzing pixel " + str(current) + " of " + str(total), end=" ") 
        print(currentTime, end="          \n")    

def recolorByThresholdMin(rawPx, threshold):
    currentR, currentG, currentB = rawPx

    if currentR < threshold:
        return True
        
    if currentG < threshold:
        return True

    if currentB < threshold:
        return True 
    
    return False

def recolorByThresholdRange(rawPx, thresholdMin, thresholdMax):
    currentR, currentG, currentB = rawPx

    if currentR < thresholdMin or currentR > thresholdMax:
        return True
        
    if currentG < thresholdMin or currentR > thresholdMax:
        return True

    if currentB < thresholdMin or currentR > thresholdMax:
        return True 
    
    return False

def recolorByHue(rawPx):
    currentHue, currentSaturation, currentValue = rawPx

    if currentHue < hueMin or currentHue > hueMax:
        return True

    if currentSaturation < saturationMin or currentSaturation > saturationMax:
        return True
    
    if currentValue < valueMin or currentValue > valueMax:
        return True

    return False

def saveFile(rgbImage, hsvImage, fileName):
    print("        | ")

    if os.path.isdir(folderOutput) == False:
        os.makedirs(folderOutput)
    if saveToLatest == True and os.path.isdir("Latest") == False:
        os.makedirs("Latest")

    if os.path.isfile(folderOutput+"/"+fileName) == False:
        # outputRgbImage = rgbImage.save(folderOutput+"/rgb-"+fileName)
        outputHsvImage = hsvImage.convert("RGB").save(folderOutput+"/hsv-"+fileName, quality=saveImageQuality)
        if saveToLatest == True:
            outputHsvImage = hsvImage.convert("RGB").save("Latest/hsv-"+fileName, quality=saveImageQuality)
        print("SUCCESS | Files saved successfully")
    else:
        print("ERROR   | There was a conflict saving this image, analysis aborted\n")