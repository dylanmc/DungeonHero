# DungeonHero
Collaboration with my 13-year old nephew

We started with some straight-line Python code he wrote. Now it's got
loops!

To run the game,
python3 hero_template.py

To edit the cave system,
python3 hero_crafter.py

The main role in hero_crafter is to dig new passages and rooms.
When you're in a room, you can choose any direction to dig, e.g., dig northeast
Then you're asked to describe the room. The game automatically creates passages in the opposite direction. If it doesn't know the opposite direction (e.g., you type `dig upwards`), it will ask you for the reverse (in this case `downwards` might make sense).

To save the file, use the save command, e.g. `save newcave.py`

If you're happy with your new cave, you can copy it over `cave_map.py`
