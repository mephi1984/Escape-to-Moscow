from PIL import Image


import glob, os

def replacePose1():
    os.chdir("E:/Work/renpyProjects/Runaway_github/game/images/sprites/Aliya/Pose1")
    for file in glob.glob("*.png"):
        if not (file.startswith("face")):
            print("Processing file: " + file)
            img = Image.open(file)
            area = (390, 297, 390+264, 297+264)
            cropped_img = img.crop(area)
            cropped_img.save("face_" + file)

def replacePose1mask():
    os.chdir("E:/Work/renpyProjects/Runaway_github/game/images/sprites/Aliya/Pose1/mask1")
    for file in glob.glob("*.png"):
        if not (file.startswith("face")):
            print("Processing file: " + file)
            img = Image.open(file)
            area = (390, 297, 390+264, 297+264)
            cropped_img = img.crop(area)
            cropped_img.save("face_" + file)
   
def replacePose2():   
    os.chdir("E:/Work/renpyProjects/Runaway_github/game/images/sprites/Aliya/Pose2")
    for file in glob.glob("*.png"):
        if not (file.startswith("face")):
            print("Processing file: " + file)
            img = Image.open(file)
            area = (450, 309, 450+264, 309+264)
            cropped_img = img.crop(area)
            cropped_img.save("face_" + file)
        
def replacePose2mask():
    os.chdir("E:/Work/renpyProjects/Runaway_github/game/images/sprites/Aliya/Pose2/mask2")
    for file in glob.glob("*.png"):
        if not (file.startswith("face")):
            print("Processing file: " + file)
            img = Image.open(file)
            area = (450, 309, 450+264, 309+264)
            cropped_img = img.crop(area)
            cropped_img.save("face_" + file)


def replacePose3():
    os.chdir("E:/Work/renpyProjects/Runaway_github/game/images/sprites/Aliya/Pose3")
    for file in glob.glob("*.png"):
        if not (file.startswith("face")) and not (file.startswith("phone")):
            print("Processing file: " + file)
            img = Image.open(file)
            area = (450, 309, 450+264, 309+264)
            cropped_img = img.crop(area)
            cropped_img.save("face_" + file)
            
def replacePose4():
    os.chdir("E:/Work/renpyProjects/Runaway_github/game/images/sprites/Aliya/Pose3")
    for file in glob.glob("*.png"):
        if not (file.startswith("face")) and not (file.startswith("phone")):
            print("Processing file: " + file)
            img = Image.open(file)
            area = (450, 309, 450+264, 309+264)
            cropped_img = img.crop(area)
            cropped_img.save("face_" + file)


def replaceSitting1():
    os.chdir("E:/Work/renpyProjects/Runaway_github/game/images/sprites/Aliya/Sitting1")
    for file in glob.glob("*.png"):
        if not (file.startswith("face")) and not (file.startswith("base")):
            print("Processing file: " + file)
            img = Image.open(file)
            area = (798, 126, 798+264, 126+264)
            cropped_img = img.crop(area)
            cropped_img.save("face_" + file)
            
def replaceSitting1alt():
    os.chdir("E:/Work/renpyProjects/Runaway_github/game/images/sprites/Aliya/Sitting1/alt")
    for file in glob.glob("*.png"):
        if not (file.startswith("face")) and not (file.startswith("base")):
            print("Processing file: " + file)
            img = Image.open(file)
            area = (830, 126, 830+264, 126+264)
            cropped_img = img.crop(area)
            cropped_img.save("face_" + file)

def replacePose4():
    os.chdir("E:/Work/renpyProjects/Runaway_github/game/images/sprites/Aliya/Pose4")
    for file in glob.glob("*.png"):
        if not (file.startswith("face")) and not (file.startswith("base")):
            print("Processing file: " + file)
            img = Image.open(file)
            area = (552, 358, 552+264, 358+264)
            cropped_img = img.crop(area)
            cropped_img.save("face_" + file)

def replaceSitting2():
    os.chdir("E:/Work/renpyProjects/Runaway_github/game/images/sprites/Aliya/Sitting2/bench")
    for file in glob.glob("*.png"):
        if not (file.startswith("face")) and not (file.startswith("base")):
            print("Processing file: " + file)
            img = Image.open(file)
            area = (332, 228, 332+264, 228+264)
            cropped_img = img.crop(area)
            cropped_img.save("face_" + file)        

replaceSitting2()



