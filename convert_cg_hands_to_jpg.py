from PIL import Image

import glob, os
from fnmatch import fnmatch



def saveToJpg():
    os.chdir("E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\CG_hands\\new")
    for file in glob.glob("*.png"):
        print("Processing file: " + file)
        img = Image.open(file)
        file = file.replace('.png', '.jpg')
        img.save(file, quality=95)
        


saveToJpg()




