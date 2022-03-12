from datetime import datetime

# --------------------------------------------------------------
# FILTERS

# YELLOW
# hueMin = 37
# hueMax = 45

hueMin = 80
hueMax = 200

saturationMin = 0
saturationMax = 255

valueMin = 50
valueMax = 255

# --------------------------------------------------------------
# SUBSTITUTE COLORS

# rgbSubstituteColor = (255,255,255)
hsvSubstituteColor = (0,0,255)

# --------------------------------------------------------------
# OTHER

folderSource = "_Source"
folderOutput = "CutOuts "+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
saveImageQuality = 255
saveToLatest = True