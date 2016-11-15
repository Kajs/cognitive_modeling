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
import math

global testNumber
testNumber = "01"

window_w = 800
window_h = 600
letters = None
exposureDurationMax = 0.5
exposureDurationMin = 0.01
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

global displayMode
global displayModeInitial
global textMode
global imgMode
displayMode = 'intro1
imgMode = "priming"
displayModeInitial = True
modeSwitchKey = key.ENTER
primingTime = 1

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
    
    answerAge = ""
    answerGender = ""
    answerProof = ""
    answerIsFamous = ""
    displayMode = "img"
    imgMode = "priming"
    letters = ""
    imagesShown += 1
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
famousPath + "50 cent.jpg",
famousPath + "Adolf Hitler.jpg",
famousPath + "Albert Einstein.jpg",
famousPath + "Angelina Jolie.jpg",
famousPath + "Arnold Swarzenegger.jpg",
famousPath + "Barack Obama.jpg",
famousPath + "Beyonce Knowles.jpg",
famousPath + "Bill Clinton.jpg",
famousPath + "Bill Gates.jpg",
famousPath + "Britney Spears.jpg",
famousPath + "Cameron Diaz.jpg",
famousPath + "Cher.jpg",
famousPath + "Christina Aguilera.jpg",
famousPath + "Donald Trump.jpg",
famousPath + "Dronning Margrethe.jpg",
famousPath + "Dr Phil.jpg",
famousPath + "Elvis Presley.jpg",
famousPath + "Eminem.jpg",
famousPath + "George W. Bush.jpg",
famousPath + "Hillary Clinton.jpg",
famousPath + "Jennifer Aniston.jpg",
famousPath + "Jennifer Lopez.jpg",
famousPath + "Jim Carrey.jpg",
famousPath + "Justin Bieber.jpg",
famousPath + "Kim Kardashian.jpg",
famousPath + "Lady Gaga.jpg",
famousPath + "Leonardo DeCaprio.jpg",
famousPath + "Madonna Louise.jpg",
famousPath + "Marylin Monroe.jpg",
famousPath + "Michael Jackson.jpg",
famousPath + "Michelle Obama.jpg",
famousPath + "Miley Cyrus.jpg",
famousPath + "Nicole Kidman.jpg",
famousPath + "Oprah Winfrey.jpg",
famousPath + "Pamela Anderson.jpg",
famousPath + "Shakira.jpg",
famousPath + "Steve Jobs.jpg",
famousPath + "Tom Cruise.jpg",
famousPath + "Vladimir Putin.jpg",
famousPath + "DUPLICATE.jpg",
notFamousPath + "AngelinaJolielookAlike.jpg",
notFamousPath + "BradPittlookAlike.jpg",
notFamousPath + "BritneySpearslookAlike.jpg",
notFamousPath + "DavidBlookAlike.jpg",
notFamousPath + "JimCareylookAlike.jpg",
notFamousPath + "KimKardashianlookAlike.jpg",
notFamousPath + "KimKlookAlike.jpg",
notFamousPath + "KlookAlike.jpg",
notFamousPath + "LeonardoDiCapookAlike.jpg",
notFamousPath + "maleNo1tFamouse.jpg",
notFamousPath + "maleNotFamouse.jpg",
notFamousPath + "Max GreenfieldLookAlike.jpg",
notFamousPath + "ModelNotFamousLookAlike.jpg",
notFamousPath + "NotFamouse.jpg",
notFamousPath + "NotFamousLookAlike.jpg",
notFamousPath + "NotSoFamouse.jpg",
notFamousPath + "NotSsoFamouse.jpg",
notFamousPath + "RihannaLookAlike.jpg",
notFamousPath + "StylistlookAlike.jpg",
notFamousPath + "SylvesterStlookAlike.jpg",

notFamousPath + "AngelinaJolielookAlike.jpg",
notFamousPath + "BradPittlookAlike.jpg",
notFamousPath + "BritneySpearslookAlike.jpg",
notFamousPath + "DavidBlookAlike.jpg",
notFamousPath + "JimCareylookAlike.jpg",
notFamousPath + "KimKardashianlookAlike.jpg",
notFamousPath + "KimKlookAlike.jpg",
notFamousPath + "KlookAlike.jpg",
notFamousPath + "LeonardoDiCapookAlike.jpg",
notFamousPath + "maleNo1tFamouse.jpg",
notFamousPath + "maleNotFamouse.jpg",
notFamousPath + "Max GreenfieldLookAlike.jpg",
notFamousPath + "ModelNotFamousLookAlike.jpg",
notFamousPath + "NotFamouse.jpg",
notFamousPath + "NotFamousLookAlike.jpg",
notFamousPath + "NotSoFamouse.jpg",
notFamousPath + "NotSsoFamouse.jpg",
notFamousPath + "RihannaLookAlike.jpg",
notFamousPath + "StylistlookAlike.jpg",
notFamousPath + "SylvesterStlookAlike.jpg"
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
    i = pyglet.image.load(path)
    center_image(i)
    sprite = pyglet.sprite.Sprite(i, window_w/2, window_h/2)
    return sprite
def getRandomImage():
    path = imagePathsRandom[r.randint(0, len(imagePathsRandom) - 1)]
    i = pyglet.image.load(path)
    center_image(i)
    sprite = pyglet.sprite.Sprite(i, window_w/2, window_h/2)
    return sprite
    
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
    global answerText
    global displayModeInitial
    global textMode
    global imgMode
    
    window.clear()
    if(displayMode == 'intro'):
        introText = 'A series of faces, some of which are famous will be displayed.'
        introText += ' Your task is to identify which are famous and which are not.'
        introText += '\n Please also try and guess the persons age and gender.'
        introText += '\n\n If you think a person is famous, provide the name.'
        introText += ' If you can\'t remember the name, please tell from where you '
        introText += 'know the person (like the name of a movie etc).'
        introText += '\n\n On all screens, press ENTER to continue.'
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
            startTime = time.time()
        img.draw()
        t = time.time()
        if (t - startTime > exposureDurations[exposureDurationPos]):
            imgMode = "random"
            displayModeInitial = True
    elif(displayMode == 'img' and imgMode == "random"):
        if(displayModeInitial):
            displayModeInitial = False
            img = getRandomImage()
        img.draw()
        t = time.time()
        if (t - startTime > exposureDurations[exposureDurationPos] + 1):
            displayMode = "text"
            textMode = "isFamous"
            displayModeInitial = True
    elif(displayMode == 'text'):
        if(displayModeInitial):
            displayModeInitial = False
            if (textMode == 'isFamous'):
                answerText = "Is the person famous?"
                answerText += "\n\n exposureDuration: " + str(exposureDurations[exposureDurationPos]) + ", imagePos: " + str(imageSequence[currentImage])
                answerText += "\n\nPress F for famous and H for not famous."
            elif(textMode == 'gender'):
                answerText = "Estimate gender on a scale of 1 to 9.\n\n 1 is very male.\n 9 is very female.\n\n Your answer: "
            elif(textMode == 'age'):
                answerText = "Estimate the persons age: "
            elif(textMode == 'proof'):
                answerText = "Please enter the persons name. If you can't remember the name, try and provide specific information related to the person (like the name of a movie they starred in).\n\n Your answer: "
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
    
    if((symbol == key.F or symbol == key.H) and ((displayMode == "text" and textMode == "isFamous") or ((displayMode == "img") and (imgMode != "priming")))):
        measuredResponseTime = time.time() - startTime
        if(symbol == key.F):
            answerIsFamous = "f"
        if(symbol == key.H):
            answerIsFamous = "h"
        displayMode = "text"
        textMode = "gender"
        displayModeInitial = True  
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
    elif symbol == modeSwitchKey and displayMode == 'intro':
        displayMode = 'img'
    elif symbol == modeSwitchKey and len(letters) > 0:
        if(displayMode == "text"):
            if(textMode == "gender"):
                answerGender = letters
                textMode = "age"
            elif textMode == "age":
                answerAge = letters
                if answerIsFamous == "h":
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
        elif (textMode == "isFamous" and symbol in validBool):
            letters = str(unichr(symbol))
            
def writeAnswers():
    with open('data/data.csv', 'a') as f:
        writer = csv.writer(f)
        if(os.stat('data/data.csv').st_size == 0):
            writer.writerow(['test_id', 'famous', 'gender', 'age', 'proof', 'exposure_duration', 'image_name', 'response_time'])
        imagePath = imagePaths[imageSequence[currentImage]]
        imagePathSub = None;
        if(imageSequence[currentImage] < len(imagePaths)/2):
            imagePathSub = imagePath[len(famousPath):]
        else:
            imagePathSub = imagePath[len(notFamousPath):]
        writer.writerow([testNumber, answerIsFamous, answerGender, answerAge, answerProof, exposureDurations[exposureDurationPos], imagePathSub, measuredResponseTime])
        f.close()
        

def scheduledWork(value):
    return value
    
pyglet.clock.schedule_interval(scheduledWork, 0.1)
pyglet.app.run()
 