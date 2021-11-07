from PIL import Image

import glob, os
from fnmatch import fnmatch


def resizeSaveFiles():
    os.chdir("E:\\Work\\renpyProjects\\Runaway_github\\game\\gui\\savegamePics")
    for file in glob.glob("*.jpg"):
        print("Processing file: " + file)
        img = Image.open(file)
        resized_img = img.resize((256,144), Image.ANTIALIAS)
        resized_img.save(file, quality=95)
        
def resizeGalleryPics():
    os.chdir("E:\\Work\\renpyProjects\\Runaway_github\\game\\gui\\galleryPics")
    for file in glob.glob("*.png"):
        print("Processing file: " + file)
        img = Image.open(file)
        resized_img = img.resize((276,164), Image.ANTIALIAS)
        resized_img.save(file)
        
def resizeGeneralBkgsPng():
    for file in glob.glob("*.png"):
        print("Processing file: " + file)
        img = Image.open(file)
        resized_img = img.resize((1280,720), Image.ANTIALIAS)
        resized_img.save(file)

def resizeGeneralBkgsJpg():
    os.chdir("E:\\Work\\renpyProjects\\Runaway_github\\game\\images")
    for file in glob.glob("*.jpg"):
        print("Processing file: " + file)
        img = Image.open(file)
        resized_img = img.resize((1280,720), Image.ANTIALIAS)
        resized_img.save(file, quality=95)
def resizeSlideShow():
    os.chdir("E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\slideshow")
    for file in glob.glob("*.jpg"):
        print("Processing file: " + file)
        img = Image.open(file)
        resized_img = img.resize((1280,720), Image.ANTIALIAS)
        resized_img.save(file, quality=95)
        
def resizeGallery():
    os.chdir("E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\gallery")
    for file in glob.glob("*.jpg"):
        print("Processing file: " + file)
        img = Image.open(file)
        resized_img = img.resize((1280,720), Image.ANTIALIAS)
        resized_img.save(file, quality=95)
        
def resizeAllSpritesTo2x():
#!!! Need to skip Sitting1 and Sitting2
    root = "E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\sprites"
    pattern = "*.png"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern) and ("Sitting1" not in path) and ("Sitting2" not in path):
                fullName = os.path.join(path, name)
                print(fullName)
                img = Image.open(fullName)
                width, height = img.size
                resized_img = img.resize((int(width/2),int(height/2)), Image.ANTIALIAS)
                resized_img.save(fullName)

def resizeAliyaSittingSpritesTo1dot5():
    root = "E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\sprites\\Aliya\\Sitting1"
    pattern = "*.png"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                fullName = os.path.join(path, name)
                print(fullName)
                img = Image.open(fullName)
                width, height = img.size
                resized_img = img.resize((int(width*2.0/3.0),int(height*2.0/3.0)), Image.ANTIALIAS)
                resized_img.save(fullName)
    root = "E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\sprites\\Aliya\\Sitting2"
    pattern = "*.png"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                fullName = os.path.join(path, name)
                print(fullName)
                img = Image.open(fullName)
                width, height = img.size
                resized_img = img.resize((int(width*2.0/3.0),int(height*2.0/3.0)), Image.ANTIALIAS)
                resized_img.save(fullName)

def resizeImagesTo1dot5_CG_hands():
    root = "E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\CG_hands"
    pattern = "*.png"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                fullName = os.path.join(path, name)
                print(fullName)
                img = Image.open(fullName)
                width, height = img.size
                resized_img = img.resize((int(width*2.0/3.0),int(height*2.0/3.0)), Image.ANTIALIAS)
                resized_img.save(fullName)


def resizeImagesTo1dot5_CG_messenger_desktop():
    root = "E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\CG_messenger_desktop"
    pattern = "*.png"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                fullName = os.path.join(path, name)
                print(fullName)
                img = Image.open(fullName)
                width, height = img.size
                resized_img = img.resize((int(width*2.0/3.0),int(height*2.0/3.0)), Image.ANTIALIAS)
                resized_img.save(fullName)


def resizeImagesTo1dot5_CG_messenger_phone():
    root = "E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\CG_messenger_phone"
    pattern = "*.png"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                fullName = os.path.join(path, name)
                print(fullName)
                img = Image.open(fullName)
                width, height = img.size
                resized_img = img.resize((int(width*2.0/3.0),int(height*2.0/3.0)), Image.ANTIALIAS)
                resized_img.save(fullName)

def resizeImagesTo1dot5_cg_screen():
    root = "E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\cg_screen"
    pattern = "*.png"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                fullName = os.path.join(path, name)
                print(fullName)
                img = Image.open(fullName)
                width, height = img.size
                resized_img = img.resize((int(width*2.0/3.0),int(height*2.0/3.0)), Image.ANTIALIAS)
                resized_img.save(fullName)



def resizeImagesTo1dot5_day4_airportPng():
    root = "E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\day4_airport"
    pattern = "*.png"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                fullName = os.path.join(path, name)
                print(fullName)
                img = Image.open(fullName)
                width, height = img.size
                resized_img = img.resize((int(width*2.0/3.0),int(height*2.0/3.0)), Image.ANTIALIAS)
                resized_img.save(fullName)


def resizeImagesTo1dot5_day4_airportJpg():
    root = "E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\day4_airport"
    pattern = "*.jpg"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                fullName = os.path.join(path, name)
                print(fullName)
                img = Image.open(fullName)
                width, height = img.size
                resized_img = img.resize((int(width*2.0/3.0),int(height*2.0/3.0)), Image.ANTIALIAS)
                resized_img.save(fullName, quality=95)
                
def resizeImagesTo1dot5_day4_room_stuff():
    root = "E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\day4_room_stuff"
    pattern = "*.png"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                fullName = os.path.join(path, name)
                print(fullName)
                img = Image.open(fullName)
                width, height = img.size
                resized_img = img.resize((int(width*2.0/3.0),int(height*2.0/3.0)), Image.ANTIALIAS)
                resized_img.save(fullName)


def resizeImagesTo1dot5_eating():
    root = "E:\\Work\\renpyProjects\\Runaway_github\\game\\images\\eating"
    pattern = "*.png"
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                fullName = os.path.join(path, name)
                print(fullName)
                img = Image.open(fullName)
                width, height = img.size
                resized_img = img.resize((int(width*2.0/3.0),int(height*2.0/3.0)), Image.ANTIALIAS)
                resized_img.save(fullName)

#resizeSaveFiles()
#resizeGalleryPics()

#resizeGeneralBkgsPng()
#resizeGeneralBkgsJpg()
#resizeSlideShow()
#resizeGallery()

#resizeAllSpritesTo2x()

resizeAliyaSittingSpritesTo1dot5()

#resizeImagesTo1dot5_CG_hands()
#resizeImagesTo1dot5_CG_messenger_desktop()
#resizeImagesTo1dot5_CG_messenger_phone()
#resizeImagesTo1dot5_cg_screen()
#resizeImagesTo1dot5_day4_airportPng()
#resizeImagesTo1dot5_day4_airportJpg()
#resizeImagesTo1dot5_day4_room_stuff()

#resizeImagesTo1dot5_eating()






