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

opposites = { "up" : "down", "north": "south", "east": "west",
        "northeast": "southwest", "northwest" : "southeast"}
# create the opposites (e.g., if we have up->down, add down->up
additions = {}
for k in opposites:
    v = opposites[k]
    additions[v] = k
opposites.update(additions)

try:
    while stillPlaying:
        line = input("what do you do? ")
        words = line.split(" ")
        cmd = words[0]
        if (cmd == 'inventory') :
            print(monsters.player['desc'])
            print ("you have: a cursed pickaxe, welded to your gloves")
        elif (cmd == 'look') :
            print(location['desc']);
            print("There are exits in these directions: ", end="")
            for exit in location['passages']:
                print(exit + " ", end="")
            print("")
        elif (cmd == 'quit') :
            print("Sorry to see you go.")
            stillPlaying = False
        elif (cmd == 'walk' or cmd == 'go') :
            dir = words[1]
            if (dir in location['passages']) :
                location = cave_map.rooms[(location['passages'])[dir]]
                time.sleep(1)
            else:
                print("You can't go that way")
        elif (cmd == 'dig') :
            if len(words) < 2:
                print("you need to choose a direction - it has to be a word")
                continue
            dir = words[1]
            if dir in opposites:
                rev_dir = opposites[dir]
            else:
                rev_dir = input("describe the opposite of " + dir + " ")
                opposites[dir] = rev_dir

            if (dir in location['passages']) :
                print("there's already a passageway in that direction")
                continue
            desc = input("Give me a detailed description of the room: ")
            new_room_id = input("Give me a one-word name for the room ")
            location['passages'][dir] = new_room_id
            cave_map.rooms[new_room_id] = { 'desc' : desc, 'passages' : { rev_dir : location }}
        elif (cmd == 'save') :
            fileh = open(words[1], 'w')
            out_str = "rooms = " + str(cave_map.rooms)
            fileh.write(out_str)
            fileh.close()

        elif (cmd == 'help') :
            print("inventory, walk, dig, look, save are things you can do, also quit.")
        else :
            print("I don't know what you mean")
except:
    print(str(cave_map.rooms))
