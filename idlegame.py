#Add prestige system once you reach certain gold
import pickle
import os
import datetime

def diffMins(t1, t2): #function to find of two times in minutes
    time_delta = (t1-t2)
    total_seconds = time_delta.total_seconds()
    minutes = total_seconds/60
    return minutes
def sharpen(crntDat): #function to increase multiplier by 10 at the cost of 1000 gold
    if (crntDat.currentGold >= 1000):
        crntDat.multiplier = crntDat.multiplier + 10
        crntDat.currentGold = crntDat.currentGold - 1000
    else:
        print("You do not have enough money to sharpen your sword! Slay more mobs.")           
class currentData: #class that stores data(current time, current gold, and current multiplier)
    def __init__(self, current_time, currentGold, multiplier):
        self.current_time = current_time
        self.currentGold = currentGold
        self.multiplier = multiplier   

currData = currentData(datetime.datetime.now(),0,10) #make currentData object
history = [] #stores history of currentData objects
filename = 'mypickle.pk'
#
if not os.path.exists(filename): #creates file if does not exist,
    with open(filename, 'wb') as fi:
        history.append(currData)
        pickle.dump(history, fi)
    currData = currentData(datetime.datetime.now(),0,10)
    print("Adventure Started, you have 0 gold and a stick.")
with open(filename, 'rb') as fi: #loads data from previous run
    history = pickle.load(fi)  
#
currData.current_time = datetime.datetime.now()
currData.currentGold = history[len(history) - 1].currentGold
currData.multiplier = history[len(history) - 1].multiplier
lastDiff = 0
if (len(history) >= 2):  #Runs if game has already been ran before
    lastDiff = diffMins(currData.current_time, history[len(history) - 1].current_time)
    print("You return from your adventure that took: " + str(lastDiff) + " minutes. Your sword grants you " + 
        str(currData.multiplier) + " gold per minute.")
    currData.currentGold += lastDiff * currData.multiplier #gold multiplier
    print("You have " + str(currData.currentGold) + "gold")
    choice = input("Would you like to sharpen? Type \"yes\" (costs 1000 gold, +10 gold/min): ")
    if (choice == "yes"):
        sharpen(currData)
    
history.append(currData)
#Saving data for next run
with open(filename, 'wb') as fi:
    pickle.dump(history, fi)
