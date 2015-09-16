__author__ = 'Akbar'
import random
import sys

gold = 100
apples = 3
appleValue = 50
peaches = 2
peachValue = 65
turn = 0

def Start():
    name = input("Hi, what is your name?")
    if name.capitalize() == "Akbar" or name.capitalize() == "Akbar26":
        print("Welcome, great one", name)
    elif name.capitalize() == "Prameeth" or name.capitalize() == "Yoh" or name.capitalize() == "Yoh1991" or name.capitalize() == "Edi":
        print("Welcome, League of Legends pro", name)
    elif name.capitalize() == "Felix" or name.capitalize() == "Hong 10" or name.capitalize() == "Hong10" or name.capitalize() == "gfloy" or name.capitalize() == "mfloy":
        print("Welcome, amazing bboy ", name, ". You should try playing League of Legends sometime", sep="")
    else:
        print("Welcome " + name + "!")
    print("The objective of this game is for the combined value of your gold and fruits to be equal to or higher than 1000 gold")
    print("You start with " + str(gold) + " gold, " + str(apples) + " apples and", peaches, "peaches")
    print("The price at which you can buy and sell apples and peaches varies during the game")
    print("Good luck " + name)
    Game()

def Game():
    global turn
    global appleValue
    global peachValue
    turn = turn + 1
    print("turn " + str(turn))

    appleFluctuation = random.randint(-10,10)
    peachFluctuation = random.randint(-10,10)

    if appleValue < 35:
        appleFluctuation = abs(appleFluctuation)
    elif appleValue > 65:
        appleFluctuation = -abs(appleFluctuation)
    appleValue = appleValue + appleFluctuation

    if peachValue < 50:
        peachFluctuation = abs(peachFluctuation)
    elif peachValue > 80:
        peachFluctuation = -abs(peachFluctuation)
    peachValue = peachValue + peachFluctuation

    print("Apples are currently valued at", appleValue)
    print("Peaches are currently valued at", peachValue)
    print("You currently have", apples, "apples,", peaches, "peaches and", gold, "gold")

    wnnaBuyApples =  input("Do you want to buy some apples? Y/N")
    if wnnaBuyApples == "Y" or wnnaBuyApples == "y":
        BuyApples()
    wnnaSellApples =  input("Do you want to sell some apples? Y/N")
    if wnnaSellApples == "Y" or wnnaSellApples == "y":
        SellApples()

    wnnaBuyPeaches = input("Do you want to buy some peaches? Y/N")
    if wnnaBuyPeaches == "Y" or wnnaBuyPeaches == "y":
        BuyPeaches()
    wnnaSellPeaches = input("Do you want to sell some peaches? Y/N")
    if wnnaSellPeaches == "Y" or wnnaSellPeaches == "y":
        SellPeaches()

    End()
    Game()

def BuyApples():
    global apples
    global gold
    buy = int(input("How many apples would you like to buy?"))
    if gold - (buy * appleValue) >= 0:
        apples = apples + buy
        gold = gold - (buy * appleValue)
        print("You now have", apples, "apples and", gold, "gold")
    else:
        print("You have insufficient funds")
        BuyApples()

def SellApples():
    global apples
    global gold
    sell = int(input("How many apples would you like to sell?"))
    if apples - sell >= 0:
        apples = apples - sell
        gold = gold + (sell * appleValue)
        print("you now have", apples, "apples and", gold, "gold")
    else:
        print("You don't have enough apples")
        SellApples()

def BuyPeaches():
    global peaches
    global gold
    buy = int(input("How many peaches would you like to buy?"))
    if gold - (buy * peachValue) >= 0:
        peaches = peaches + buy
        gold = gold - (buy * peachValue)
        print("You now have", peaches, "peaches and", gold, "gold")
    else:
        print("You have insufficient funds")
        BuyPeaches()

def SellPeaches():
    global peaches
    global gold
    sell = int(input("How many peaches would you like to sell?"))
    if peaches - sell >= 0:
        peaches = peaches - sell
        gold = gold + (sell * peachValue)
        print("you now have", peaches, "peaches and", gold, "gold")
    else:
        print("You don't have enough peaches")
        SellPeaches()

def End():
    if gold + (apples * appleValue) >= 1000:
        print("You Win!")
        sys.exit()
    elif gold + (apples * appleValue) <= 0:
        print("You Lose!")
        sys.exit()

Start()