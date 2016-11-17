# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 07:13:49 2016

@author: nezer
"""
import csv
import matplotlib.pyplot as plt

famousPath = "images/famous/"
notFamousPath = "images/not_famous/"
imagePaths = [
famousPath + "Albert Einstein.jpg",
famousPath + "Barack Obama.jpg",
famousPath + "Michael Jackson.jpg",
famousPath + "Steve Jobs.jpg",
famousPath + "Elvis Presley.jpg",
famousPath + "Donald Trump.jpg",
famousPath + "Justin Bieber.jpg",
famousPath + "Jim Carrey.jpg",
famousPath + "Miley Cyrus.jpg",
famousPath + "Jennifer Aniston.jpg",
famousPath + "Michelle Obama.jpg",
famousPath + "Beyonce Knowles.jpg",
famousPath + "Dronning Margrethe.jpg",
famousPath + "Angelina Jolie.jpg",
famousPath + "Oprah Winfrey.jpg",
famousPath + "Britney Spears.jpg",
notFamousPath + "NotFamousM1.png",
notFamousPath + "NotFamousM2.png",
notFamousPath + "NotFamousM3.png",
notFamousPath + "NotFamousM4.png",
notFamousPath + "NotFamousM5.png",
notFamousPath + "NotFamousW1.png",
notFamousPath + "NotFamousW2.png",
notFamousPath + "NotFamousW3.png",
notFamousPath + "NotFamousW4.png",
notFamousPath + "NotFamousW5.png",
notFamousPath + "DavidBlookAlike.jpg",
notFamousPath + "NotFamouse.jpg",
notFamousPath + "NotFamousLookAlike.jpg",
notFamousPath + "BritneySpearslookAlike.jpg",
notFamousPath + "JimCareylookAlike.jpg",
notFamousPath + "RihannaLookAlike.jpg"
]
famousYes = "Y"
famousNo = "N"

correctFamous = [[],[]]
incorrectFamous = [[],[]]
correctNotFamous = [[],[]]
incorrectNotFamous = [[],[]]

with open('data/data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    firstLine = True
    for row in reader:
        if firstLine:
            firstLine = False
            print row
        else:
            responseTime = row[7]
            exposureDuration = row[5]
            answerFamous = row[1]
            imageName = row[6]
            print exposureDuration
            if(famousPath + imageName) in imagePaths:
                if answerFamous == famousYes:
                    correctFamous[0].append(exposureDuration);
                    correctFamous[1].append(responseTime);
                else:
                    incorrectFamous[0].append(exposureDuration);
                    incorrectFamous[1].append(responseTime);
            elif(notFamousPath + imageName) in imagePaths:
                if answerFamous == famousNo:
                    correctNotFamous[0].append(exposureDuration);
                    correctNotFamous[1].append(responseTime);
                else:
                    incorrectNotFamous[0].append(exposureDuration);
                    incorrectNotFamous[1].append(responseTime);
        
plt.scatter(correctFamous[0], correctFamous[1])
plt.ylabel('Response Time')
plt.xlabel('Exposure Duration')
plt.title('Correct Famous')
plt.show()            

plt.scatter(incorrectFamous[0], incorrectFamous[1])
plt.ylabel('Response Time')
plt.xlabel('Exposure Duration')
plt.title('Incorrect Famous')
plt.show()  

plt.scatter(correctNotFamous[0], correctNotFamous[1])
plt.ylabel('Response Time')
plt.xlabel('Exposure Duration')
plt.title('Correct Not Famous')
plt.show()            

plt.scatter(incorrectNotFamous[0], incorrectNotFamous[1])
plt.ylabel('Response Time')
plt.xlabel('Exposure Duration')
plt.title('Incorrect Not Famous')
plt.show()

print 1.0/60 