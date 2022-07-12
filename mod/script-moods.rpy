init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="peMod_mood_pms",
            prompt="...PMS symptoms.",
            category=[store.mas_moods.TYPE_BAD]
        ),
        code="MOO"
    )

label peMod_mood_pms:
    m 7ekc "Aw [player], I'm sorry you're feeling that way."
    m 3etd "Is there a certain emotion you're feeling now - sad or irritated?"
    m 1eka "Well, whatever you're feeling, please know that it's completely valid and that you're not weak nor overemotional."
    m 1esa "And if you need to rant I'm always here to listen."
    m 3hua "I hope you get to feel more like yourself soon."
    m 1ekb "Oh and [mas_get_player_nickname()], please know that I would never judge you for something you can't control."
    m 3hubsu "I love you so so much."
    m 3hubsb "Your girlfriend is here for you!"
    return "love"


init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="peMod_mood_cramps",
            prompt="...pain from cramps.",
            category=[store.mas_moods.TYPE_BAD]
        ),
        code="MOO"
    )

label peMod_mood_cramps:
    m 2wkd "Oh no [player]!"
    m 1dkc "I'm really sorry you're not feeling good right now."
    m 3wksdld "Is there anything I can do to help? Maybe let you rant about the pain or hold you?"
    m 3wksdlc "I could also give you some tips to help with it as well!"
    m 2rkd "I'm sorry, I'm panicking aren't I..."
    m 2dkc "I just love you so much and I hate to see you in pain."
    m 1eka "Well anyway [mas_get_player_nickname()], I hope you start feeling better and maybe try running yourself a hot bath."
    m 3ekb "Or putting your legs up and doing something you love."
    m 1eka "Please do take care of yourself."
    return "love"
