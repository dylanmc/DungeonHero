"""
Hero_template

Description:
"""
import random
import sys
import cave_map
import time

stillPlaying = True
inventory = ["great sword", "musket", "short sword", "mace", "cup of tea", "pocket calculator" ]
equipped = 0
timePassed = False
battle = False
playerHealth = 10
location = cave_map.rooms["entrance_r"]

while stillPlaying:
    line = input("what do you do? ")
    words = line.split(" ")
    cmd = words[0]
    if (cmd == 'inventory') :
        print ("you have:")
        for i in range(len(inventory)):
            print (str(i) + ": " + inventory[i])
        print ("you have equipped your " + inventory[equipped])
    elif (cmd == 'look') :
        print(location['desc']);
    elif (cmd == 'equip'):
        equipped = int(words[1])
    elif (cmd == 'quit') :
        print("Sorry to see you go.")
        stillPlaying = False
    elif (cmd == 'walk' or cmd == 'go') :
        timePassed = True
        dir = words[1]
        if (dir in location['passages']) :
            location = cave_map.rooms[(location['passages'])[dir]]
            time.sleep(3)
        else:
            print("You can't go that way")
    elif (cmd == 'help') :
        print("inventory, walk, equip, look are things you can do, also quit.")
    else :
        print("I don't know what you mean")
    if timePassed and random.randint(1, 100) < 25:
        print("A monster jumps in front of you!")
        battle = True
    while battle:
        line = input("What do you do?")
        words = line.split(" ")
        cmd = words[0]
        if cmd == 'help':
            print("attack, dodge, defend, focus are your options")
        elif cmd == 'attack':
            # do stuff
            print("you attack the monster")
        elif cmd == 'dodge' :
            # do more stuff
            print("you dodge")
        elif cmd == 'defend' :
            # you know...
            print("you defend")
        elif cmd == 'focus' :
            # more stuff
            print("you sit down with your pocket calculator and focus")
        if playerHealth <= 0:
            print ("Sorry to say, you've died.")
            system.exit(0)
