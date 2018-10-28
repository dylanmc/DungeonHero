
rooms = {
    "entrance_r": {
        'desc' : "You are in the entrance to a huge cave system. The way you entered has collapsed behind you."
        , 'passages' : { "north": "passage_r" }
        , 'occupants': True
        , 'hostile' : False
        }
    , "passage_r": {
        'desc' : "This is a long low north-south passage"
        , 'passages' : {
            "south": "entrance_r"
            , "north": "grand_chamber_r"
            }
        , 'occupants': True
        , 'hostile': True
        }
    , "grand_chamber_r": {
        'desc' : "You stumble in to a grand chamber, dimly lit by phosphorescent rocks around its perimeter. You can make out a number of passages leading off in various directions."
        , 'passages' : {
            "south": "passage_r"
            , "north": "crossroads_r"
            }
        , 'occupants': True
        , 'hostile': True
        }
    , "crossroads_r": {
        'desc' : "You enter a large, high-ceilinged room. There is a dead knight in one corner."
        , 'passages' : {
            "south": "grand_chamber_r"
        }
        , 'make_occupant':'ogre'
    }
}
