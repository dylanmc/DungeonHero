"""
Hero_template

Description:
"""
import random
import sys
import cave_map
import monsters
import time

stillPlaying = True
inventory = ["great sword", "musket", "short sword", "mace", "cup of tea", "pocket calculator" ]
equipped = 0
timePassed = False
battle = False
playerHealth = 10
location = cave_map.rooms["entrance_r"]
monster = None
player = monsters.player

while stillPlaying:
    line = input("what do you do? ")
    words = line.split(" ")
    cmd = words[0]
    if (cmd == 'inventory') :
        print(monsters.player['desc'])
        print ("you have:")
        for i in range(len(inventory)):
            print (str(i) + ": " + inventory[i])
        print ("you have equipped your " + inventory[equipped])
    elif (cmd == 'look') :
        print(location['desc']);
        print("There are exits in these directions: ", end="")
        for exit in location['passages']:
            print(exit + " ", end="")
        print("")

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
            time.sleep(1)
        else:
            print("You can't go that way")
    elif (cmd == 'help') :
        print("inventory, walk, equip, look are things you can do, also quit.")
    else :
        print("I don't know what you mean")
    if timePassed and random.randint(1, 100) < 50:
        # TODO: each room has a pool of monsters, easy monsters on
        # early rooms
        dieRoll = random
        monster = dict(monsters.monsters[random.randint(0,len(monsters.monsters))-1])
        print("A " + monster['desc'] + " jumps in front of you!")
        battle = True
        while battle:
            line = input("What do you do?")
            words = line.split(" ")
            cmd = words[0]
            if cmd == 'help':
                print("attack, dodge, defend, focus are your options")
            elif cmd == 'attack':
                print("you attack the monster")
                # TODO: roll a die and see if there are crit damage
                if (monsters.player['speed'] < monster['speed']) :
                    # monster has advantage
                    player['health'] = player['health'] - monster['attack']
                    if (monsters.player['health'] <= 0) :
                        print("You died.")
                        sys.exit(0);
                    monster['health'] = monster['health'] - player['attack']
                    if (monster['health'] <= 0):
                        print("You killed the " + monster['desc'] + "!")
                        battle = False
                else:
                    # player has advantage
                    monster['health'] = monster['health'] - player['attack']
                    if (monster['health'] <= 0):
                        print("You killed the " + monster['desc'] + "!")
                        battle = False
                    player['health'] = player['health'] - monster['attack']
                    if (player['health'] <= 0) :
                        print("You died.")
                        sys.exit(0);

            elif cmd == 'dodge' :
                print("you dodge")
            elif cmd == 'defend' :
                # you know...
                print("you defend")
            elif cmd == 'focus' :
                # more stuff
                print("you sit down with your pocket calculator and focus")

            print("Your health is " + str(player['health']))
            print("The " + monster['desc'] + "'s health is " + str(monster['health']))
        # the battle is over
        monster = None

