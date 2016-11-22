# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 09:22:29 2016

@author: nezer
"""
import pyglet 
import csv
from pyglet.window import key 
import time
import os
import random as r
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

global testNumber
testNumber = "15"

global contrastAmount
global colorAmount
global blurAmount
contrastAmount = 0.2
colorAmount = 0.0
blurAmount = 5.5

window_w = 800
window_h = 600
letters = None
exposureDurationMult = 1.0/60.0
exposureDurationMax = exposureDurationMult * 18
exposureDurationMin = exposureDurationMult * 2.5
imagesShown = 0
global currentImage
currentImage = 0
imagesToShow = 2
updateInterval = 1
measuredResponseTime = 0

global lettes
global pressedKey
global answerText
answerText = ''
letters = answerText
presseKey = ''
fontSize = 20

global textOnDisplay
global img
global imgRandom

global displayMode
global displayModeInitial
global textMode
global imgMode
displayMode = 'intro1'
imgMode = "priming"
displayModeInitial = True
modeSwitchKey = key.ENTER
primingTime = 2.5
famousKey = "Y"
notFamousKey = "N"
notAnsweredInTimeKey = ["U", "U" + famousKey, "U" + notFamousKey]
global isFamousAnswered
isFamousAnswered = False

global startTime

global answerAge
global answerGender
global answerProof
global answerIsFamous
global writer
    
def reset():
    global answerAge
    global answerGender
    global answerProof
    global answerIsFamous
    global displayMode
    global letters
    global currentImage
    global imagePaths
    global imagesShown
    global exposureDurationPos
    global imgMode
    global isFamousAnswered
    global measuredResponseTime
    
    answerAge = ""
    answerGender = ""
    answerProof = ""
    answerIsFamous = ""
    isFamousAnswered = False
    displayMode = "img"
    imgMode = "priming"
    letters = ""
    imagesShown += 1
    measuredResponseTime = 0
    if(imagesShown == imagesToShow * 2):
        exposureDurationPos += 1
        imagesShown = 0
    currentImage += 1
    if(currentImage == len(imagePaths)):
        displayMode = "finished"            

validLetters = [
key.A, key.B, key.C,
key.D, key.E, key.F,
key.G, key.H, key.I,
key.J, key.K, key.L,
key.M, key.N, key.O,
key.P, key.Q, key.R,
key.S, key.T, key.U,
key.V, key.W, key.X,
key.Y, key.Z, key.PERIOD,
key.SPACE]

validNumbers = [
key._0, key._1, key._2,
key._3, key._4, key._5,
key._6, key._7, key._8,
key._9]

famousPath = "images/famous/"
notFamousPath = "images/not_famous/"
imagePaths = [
famousPath + "Arnold Swarzenegger.jpg",
famousPath + "Bill Clinton.jpg",
notFamousPath + "maleNo1tFamouse.jpg",
notFamousPath + "KimKlookAlike.jpg",
]

randomPath = "images/random/"
imagePathsRandom = [
randomPath + "download.jpeg",
randomPath + "365165-800x600.jpg",
randomPath + "470668-800x600.jpg",
randomPath + "1000732.jpg",
randomPath + "1015661.jpg",
randomPath + "1099140.jpg",
randomPath + "AAEAAQAAAAAAAAWfAAAAJDcwZWVjMzIyLWIxODItNDA0Ny05MTBlLTNiMmU5OTU4ODIyNA.jpg",
randomPath + "AAEAAQAAAAAAAAZWAAAAJDVlZGI1ODUzLWRjNTMtNDg5Yy1hZDBiLTRjYTIyOGNiZTVjMg.jpg",
randomPath + "dreamstime_s_32258676.jpg",
randomPath + "iStock_000063177421_Small.jpg",
randomPath + "placeimg_800_600_any.jpg",
randomPath + "placeimg_800_600_any (1).jpg",
randomPath + "placeimg_800_600_any (2).jpg",
randomPath + "placeimg_800_600_any (3).jpg",
randomPath + "placeimg_800_600_any (4).jpg",
randomPath + "rocks-along-river_thumb[1].jpg"
]

blurSuffix = "_BLUR.jpg"

imageSequence = []
remainingFamousImages = imagesToShow
remainingNotFamousImages = imagesToShow
while len(imageSequence) < len(imagePaths):
    if(remainingFamousImages == 0 and remainingNotFamousImages == 0):
        remainingFamousImages = imagesToShow
        remainingNotFamousImages = imagesToShow
    i = 0
    if(r.random() <= 0.5):
        if(remainingFamousImages > 0):
            i = r.randint(0, len(imagePaths)/2 - 1)
            if(i not in imageSequence):
                imageSequence.append(i)
                remainingFamousImages -= 1
    else:
        if(remainingNotFamousImages > 0):
            i = r.randint(len(imagePaths)/2, len(imagePaths) - 1)
            if(i not in imageSequence):
                imageSequence.append(i)
                remainingNotFamousImages -= 1
                
exposureDurations = []
for i in range(0, len(imagePaths)/(imagesToShow*2)):
    exposureDurations.append(exposureDurationMax - i * (exposureDurationMax - exposureDurationMin)/((len(imagePaths))/(imagesToShow*2.0)))
r.shuffle(exposureDurations)
exposureDurationPos = 0

validBool = [key.Y, key.N]


def center_image(image): 
    image.anchor_x = image.width/2 
    image.anchor_y = image.height/2
def getCenteredSprite():
    path = imagePaths[imageSequence[currentImage]]
    makeBlurredImage()
    i = pyglet.image.load(path[:-4] + blurSuffix)
    center_image(i)
    sprite = pyglet.sprite.Sprite(i, window_w/2, window_h/2)
    return sprite
def getRandomImage():
    global contrastAmount
    global colorAmount
    global blurAmount
    
    path = imagePathsRandom[r.randint(0, len(imagePathsRandom) - 1)]
    img = Image.open(path)
    
    converter = ImageEnhance.Color(img)
    img = converter.enhance(colorAmount)
    
    blurred_image = img.filter(ImageFilter.GaussianBlur(blurAmount))
    
    converter = ImageEnhance.Contrast(blurred_image)
    blurred_image = converter.enhance(contrastAmount) 
    
    pathNoExtension = path[:-4]
    blurred_image.save(pathNoExtension + blurSuffix)
    
    img = pyglet.image.load(pathNoExtension + blurSuffix)
    center_image(img)
    
    sprite = pyglet.sprite.Sprite(img, window_w/2, window_h/2)
    return sprite
    
def makeBlurredImage():
    global contrastAmount
    global colorAmount
    global blurAmount
    
    if False: #if you want to adjust blur/contrast and see results for all images, set to true
        for temp in imageSequence:
            path = imagePaths[temp]
            img = Image.open(path)
            converter = ImageEnhance.Color(img)
            img = converter.enhance(colorAmount)
            blurred_image = img.filter(ImageFilter.GaussianBlur(blurAmount))
            converter = ImageEnhance.Contrast(blurred_image)
            blurred_image = converter.enhance(contrastAmount)
            pathNoExtension = path[:-4]
            blurred_image.save(pathNoExtension + blurSuffix)
        
    path = imagePaths[imageSequence[currentImage]]
    img = Image.open(path)
    
    converter = ImageEnhance.Color(img)
    img = converter.enhance(colorAmount)
    
    blurred_image = img.filter(ImageFilter.GaussianBlur(blurAmount))
    
    converter = ImageEnhance.Contrast(blurred_image)
    blurred_image = converter.enhance(contrastAmount)    
    
    pathNoExtension = path[:-4]
    blurred_image.save(pathNoExtension + blurSuffix)
    
def makeLabel(text, pos_x, pos_y, f_size):

    label = pyglet.text.Label(text,
                          font_name='Times New Roman',
                          font_size=f_size,
                          x=pos_x, y=pos_y,
                          anchor_x='center', anchor_y='center',
                          multiline = True,
                          width = 512)
    return label


window = pyglet.window.Window(window_w, window_h)
keys = key.KeyStateHandler()
window.push_handlers(keys)
                
@window.event 
def on_draw():
    global letters
    global newImage
    global startTime
    global displayMode
    global showIntroduction
    global textOnDisplay
    global img
    global imgRandom
    global answerText
    global displayModeInitial
    global textMode
    global imgMode
    global isFamousAnswered
    global answerIsFamous
    
    window.clear()
    if(displayMode == 'intro1'):
        introText = "Introduction page 1 of 2\n\n"
        introText += '    A series of faces, some of which are famous will be displayed. Your task is to identify who is famous and who is not.'
        introText += '\n\nPress ENTER to continue.'
        textOnDisplay = makeLabel(introText, window_w/2, window_h/2, 20);
        textOnDisplay.draw()
    elif(displayMode == 'intro2'):
        introText = "Introduction page 2 of 2\n\n"
        introText += '    You need to make the famous/not famous decision fast using ' + famousKey
        introText += ' for YES to famous or ' + notFamousKey + ' for NO to famous.'
        introText += '\n\n Before the image is shown, a BIG exclamation mark (!) will appear for ' + str(primingTime)
        introText += ' second(s).'

        introText += '\n\n IMPORTANT: you do not need to wait for the image to disappear when you anwer.'
        introText += '\n\n Please place your fingers on ' + famousKey + ' and ' + notFamousKey + ' and press ENTER to continue.'
        textOnDisplay = makeLabel(introText, window_w/2, window_h/2, 20);
        textOnDisplay.draw()
    elif(displayMode == 'img' and imgMode == "priming"):
        if(displayModeInitial):
            displayModeInitial = False
            startTime = time.time()
        w = 0.0
        h = 0.0
        w += window_w
        h += window_h
        textOnDisplay = makeLabel("!", w/1.25, h/2, 120);
        textOnDisplay.draw()
        t = time.time()
        if(t - startTime > primingTime):
            imgMode = "normal"
            displayModeInitial = True
    elif(displayMode == 'img' and imgMode == "normal"):
        if(displayModeInitial):
            displayModeInitial = False
            img = getCenteredSprite()
            imgRandom = getRandomImage()
            startTime = time.time()
        img.draw()
        t = time.time()
        if (t - startTime > exposureDurations[exposureDurationPos]):
            imgMode = "random"
    elif(displayMode == 'img' and imgMode == "random"):
        imgRandom.draw()
        t = time.time()
        if (t - startTime > 2 - exposureDurations[exposureDurationPos]):
            displayMode = "text"
            textMode = "gender"
            displayModeInitial = True
            if(not isFamousAnswered):
                answerIsFamous = notAnsweredInTimeKey[0]
    elif(displayMode == 'text'):
        if(displayModeInitial):
            displayModeInitial = False
            if (textMode == 'isFamous'):
                answerText = "Is the person famous?"
                #answerText += "\n\n exposureDuration: " + str(exposureDurations[exposureDurationPos]) + ", imagePos: " + str(imageSequence[currentImage])
                answerText += "\n\nPress " + famousKey + ' for famous or ' + notFamousKey + ' for not famous.'
                if(isFamousAnswered):
                    textMode = "gender"
                    displayModeInitial = True
            elif(textMode == 'gender'):
                answerText = "      Estimate gender on a scale of 1 to 9:\n\n"
                answerText += "       1           3           5           7           9"
                answerText += "\n\nvery male             middle           very female"
                answerText += '\n\n\nUse number keys to answer and ENTER to proceed.'
                answerText += "\n                       Your answer: "
                answerText += letters
            elif(textMode == 'age'):
                answerText = "User number keys to answer and ENTER to proceed.\n\n"
                answerText += "Estimate the persons age: "
            elif(textMode == 'proof'):
                answerText = "Please enter the persons name.\n\n    If you can't remember the name, try and provide specific information related to the person (like the name of a movie they starred in).\n\n    If you do not know, please write 'not sure' or similar.\n\n Your answer: "
        label = makeLabel(answerText + letters, window_w/2, window_h/2, fontSize)
        label.draw()
        
    elif(displayMode == 'finished'):
        label = makeLabel("You have reached the end of the test, thank you for participating!", window_w/2, window_h/2, fontSize)
        label.draw()

        
@window.event
def on_key_press(symbol, modifiers):
    global measuredResponseTime
    global answerIsFamous
    global displayMode
    global textMode
    global displayModeInitial
    global imgMode
    global isFamousAnswered
    if((symbol in validBool) and ((displayMode == "text" and textMode == "isFamous") or ((displayMode == "img") and (imgMode != "priming")))):
        measuredResponseTime = time.time() - startTime
        if(symbol == validBool[0]):
            answerIsFamous = famousKey
        if(symbol == validBool[1]):
            answerIsFamous = notFamousKey
        isFamousAnswered = True
        if(displayMode == "text" and textMode == "isFamous"):
            displayModeInitial = True
    elif((symbol in validBool and answerIsFamous in notAnsweredInTimeKey) and (displayMode == 'text' and textMode == 'gender')):
        answerIsFamous = notAnsweredInTimeKey[0] + (chr(symbol)).upper()
        measuredResponseTime = time.time() - startTime
@window.event
def on_key_release(symbol, modifiers):
    global letters
    global displayMode
    global displayModeInitial
    global pressedKey
    global textMode
    
    global answerAge
    global answerGender
    global answerProof
    global answerIsFamous
    global measuredResponseTime
    global startTime
        
    if symbol == key.BACKSPACE and len(letters) > 0:
        letters = letters[:-1]
    elif symbol == modeSwitchKey and displayMode == 'intro1':
        displayMode = "intro2"
    elif symbol == modeSwitchKey and displayMode == 'intro2':
        displayMode = 'img'
    elif symbol == modeSwitchKey and len(letters) > 0:
        if(displayMode == "text"):
            if(textMode == "gender"):
                answerGender = letters
                textMode = "age"
            elif textMode == "age":
                answerAge = letters
                if answerIsFamous == notFamousKey:
                    answerProof = "blank"
                    writeAnswers()
                    reset()
                else:
                    textMode = "proof"
            elif textMode == "proof":
                answerProof = letters
                writeAnswers()
                reset()
            letters = ""
        displayModeInitial = True
    elif displayMode == "text":
        if textMode == "proof" and (symbol in validLetters or symbol in validNumbers):
            letters += str(unichr(symbol))
        elif (textMode == "age" and symbol in validNumbers and len(letters) < 3):
            letters += str(unichr(symbol))
        elif (textMode == "gender" and symbol in validNumbers):
            letters = str(unichr(symbol))
            
def writeAnswers():
    pass
        

def scheduledWork(value):
    return value
    
pyglet.clock.schedule_interval(scheduledWork, 0.0001)
pyglet.app.run()
 