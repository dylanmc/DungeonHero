
rooms = {
        "entrance_r": {
            'desc' : "You are in the entrance to a huge cave system. The way you entered has collapsed behind you."
            , 'passages' : { "north": "passage_r" }
            }
        , "passage_r": {
            'desc' : "This is a long low north-south passage"
            , 'passages' : {
                "south": "entrance_r"
                , "north": "grand_chamber_r"
                }
            }
        , "grand_chamber_r": {
            'desc' : "You stumble in to a grand chamber, dimly lit by phosphorescent rocks around its perimeter. You can make out a number of passages leading off in various directions."
            , 'passages' : {
                "south": "passage_r"
            }
        }
    }
