
import os
from PIL import Image
from datetime import datetime
from app.utils import *
from app.processImages import *

Image.MAX_IMAGE_PIXELS = None

print("\r\n\n\nRUNNING SCRIPT...")

# --------------------------------------------------------------

processAllImages()

# --------------------------------------------------------------

print("\r\n\nDONE!\n\n\n")