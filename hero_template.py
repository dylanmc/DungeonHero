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

# doctor up our monsters:
for m in monsters.monsters :
    monsters.monsters[m]['hostile'] = True
    monsters.monsters[m]['desc'] = m

def makeOccupants(loc):
    if not 'occupant' in loc:
        if 'make_occupant' in loc:
            loc['occupant'] = dict(monsters.monsters[loc['make_occupant']])
        elif 'occupants' in loc:
            if loc['hostile']:
                print("making a monster")
            else:
                print("making a friend")

def enterRoom(loc, d):
    if (d in loc['passages']) :
        loc = cave_map.rooms[(loc['passages'])[d]]
    else:
        print("You can't go that way")
    return loc

def describeLocation(l):
    print(l['desc'])
    if 'occupant' in l and not l['occupant'] == None:
        m = l['occupant']
        print("There is a " + m['desc'] + " in the room with you")

def handleBattle(loc, p):
    if 'occupant' in loc and not loc['occupant'] == None:
        monster = loc['occupant']
        if monster['hostile']:
            print(monster['desc'] + " attacks!")
            """
            monsterName = random.choice(list(monsters.monsters.keys()))
            monster = monsters.monsters[monsterName]
            monster['desc'] = monsterName
            print("A " + monster['desc'] + " jumps in front of you!")
            """
            battle = True
            while battle:
                line = input("(In battle) what do you do? ")
                words = line.split(" ")
                cmd = words[0]
                if cmd == 'help':
                    print("attack, dodge, defend, focus, flee are your options")
                elif cmd == 'attack':
                    print("you attack the monster")
                    # TODO: roll a die and check for crit success/failure
                    if (p['speed'] < monster['speed']) :
                        # monster has advantage
                        p['health'] = p['health'] - monster['attack']
                        if (p['health'] <= 0) :
                            print("You died.")
                            sys.exit(0);
                        monster['health'] = monster['health'] - p['attack']
                        if (monster['health'] <= 0):
                            print("You killed the " + monster['desc'] + "!")
                            loc['occupant'] = None
                            loc['inventory'] = "a dead monster"
                            battle = False
                    else:
                        # player has advantage
                        monster['health'] = monster['health'] - p['attack']
                        if (monster['health'] <= 0):
                            print("You killed the " + monster['desc'] + "!")
                            battle = False
                        p['health'] = p['health'] - monster['attack']
                        if (p['health'] <= 0) :
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
                elif cmd == 'flee' :
                    if monster['speed'] > p['speed']:
                        print("Sorry, your adversary is too fast for you")
                    else:
                        dir = words[1]
                        print("You try to flee " + dir)
                        if (dir in loc['passages']) :
                            loc = cave_map.rooms[(loc['passages'])[dir]]
                            battle = False
                            monster = None
                            if not ('seen' in loc):
                                print(" and you narrowly escape")
                                print(loc['desc'])
                                loc['seen'] = True
                            break
                        else:
                            print(" but you run into a wall instead")


                print("Your health is " + str(p['health']))
                print("The " + monster['desc'] + "'s health is " + str(monster['health']))
    # the battle is over
    monster = None
    return loc

# this is the main program
while stillPlaying:
    if not ('seen' in location):
        location['seen'] = True
        makeOccupants(location)
        describeLocation(location)
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
        location = enterRoom(location, dir)
        if not ('seen' in location):
            location['seen'] = True
            makeOccupants(location)
            describeLocation(location)
    elif (cmd == 'help') :
        print("inventory, walk, equip, look are things you can do, also quit.")
    else :
        print("I don't know what you mean")

    location = handleBattle(location, player)

