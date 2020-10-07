# Beau Kelsch
# 10/02/2020
# OOP Version of Game

import random

#class player(self):
#    self.playerName = playerName
#    self.playerGameScore = 0
#    self.playerTotalScore = 0
#    self.playerUpvoteScore = 0
#    self.playerTurn = False
#    self.playerRoundNum = 1
#    self.roundAnswers = [0]

letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
catigories = ["Animal", "Car", "Room", "State", "City", "Country", "Sports Team", "Boy's Name", "Girl's Name", "Item found in the kitchen", "Board game"]
gameCats = [0]


def catShuff():
    gameLen = int(input("How many questions?\n"))
    gameLenCount = gameLen
    for i in catigories:
        if gameLenCount > 0:
            c = catigories[random.randint(0, 10)]
            gameCats.append(c)
            gameLenCount = gameLenCount - 1
    gameCats.pop(0)

print (gameCats)
# Mainloop
print ("To begin the game, we need to create players.")
gameplayers = int(input("How many players?\n"))
games = int(input("Thank you.\nHow many games would you like to play?\n"))
# Need to create a player profile
for i in player:
    if games > 0:
        catShuff()
        l = letter[random.randint(0, 25)]
        print ("Your letter will be ", l)
        print (gameCats)
    playerAnswers = [0]
#    for i in gameCats:
#        a = input[gamecat[i]]
#        playerAnswers.append(a)
    games = games - 1

