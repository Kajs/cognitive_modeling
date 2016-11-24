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
famousPath + "Christina Aguilera.jpg",
famousPath + "Michelle Obama.jpg",
famousPath + "Beyonce Knowles.jpg",
famousPath + "Lady Gaga.jpg",
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
notFamousPath + "KlookAlike.jpg",
notFamousPath + "NotFamousLookAlike.jpg",
notFamousPath + "NotSoFamouse.jpg",
notFamousPath + "maleNotFamouse.jpg",
notFamousPath + "StylistlookAlike.jpg"
]
famousYes = "Y"
famousNo = "N"

correctFamous = [[],[]]
incorrectFamous = [[],[]]
correctNotFamous = [[],[]]
incorrectNotFamous = [[],[]]
correct = {}
incorrect = {}
invalidRows = [5, 13, 15]

with open('data/data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    firstLine = True
    for row in reader:
        if firstLine:
            firstLine = False
            print row
        else:
            testId = int(row[0])
            responseTime = row[7]
            exposureDuration = row[5]
            answerFamous = row[1]
            imageName = row[6]
            if(testId in invalidRows):
                #print "skipping testId " + str(testId)
                continue
                
            if(not correct.has_key(exposureDuration)):
                correct[exposureDuration] = 0.0
            if(not incorrect.has_key(exposureDuration)):
                incorrect[exposureDuration] = 0.0
            if(famousPath + imageName) in imagePaths:
                if answerFamous == famousYes:
                    correctFamous[0].append(exposureDuration);
                    correctFamous[1].append(responseTime);
                    correct[exposureDuration] += 1.0
                else:
                    incorrectFamous[0].append(exposureDuration);
                    incorrectFamous[1].append(responseTime);
                    incorrect[exposureDuration] += 1.0
            elif(notFamousPath + imageName) in imagePaths:
                if answerFamous == famousNo:
                    correctNotFamous[0].append(exposureDuration);
                    correctNotFamous[1].append(responseTime);
                    correct[exposureDuration] += 1.0
                    
                else:
                    incorrectNotFamous[0].append(exposureDuration);
                    incorrectNotFamous[1].append(responseTime);
                    incorrect[exposureDuration] += 1.0
            else:
                print "Image path not found: " + imageName
        
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

correctAsArray = [[],[]]
incorrectAsArray = [[],[]]

for key in correct:
    correctAsArray[0].append(key)
    correctAsArray[1].append(correct[key])
for key in incorrect:
    incorrectAsArray[0].append(key)
    incorrectAsArray[1].append(incorrect[key])
    
plt.scatter(correctAsArray[0], correctAsArray[1])
plt.ylabel('Correct')
plt.xlabel('Exposure Duration')
plt.title('Overall Correct Answers')
plt.show() 

plt.scatter(incorrectAsArray[0], incorrectAsArray[1])
plt.ylabel('Incorrect')
plt.xlabel('Exposure Duration')
plt.title('Overall Incorrect Answers')
plt.show() 

avoidDivisionByZero = 100.0
correctOverNotCorrect = [[],[]]
for key in correct:
    correctOverNotCorrect[0].append(key)
    correctOverNotCorrect[1].append((correct[key]+avoidDivisionByZero)/(incorrect[key]+avoidDivisionByZero))
plt.scatter(correctOverNotCorrect[0], correctOverNotCorrect[1])
plt.ylabel("Correct/Not correct")
plt.xlabel("Exposure Duration")
plt.title("Correct divided by incorrect answers")
plt.show()
print "\n"
for key in correct:
    print "exposure =", key + ", correct =", str(correct[key]) + ", incorrect =", incorrect[key]