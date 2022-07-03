init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="peMod_mood_pms",
            prompt="...PMS symptoms.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label peMod_mood_pms:
    m "Aw [player], I'm sorry you're feeling that way."
    m "Is there a certain emotion you're feeling now - sad or irritated?"
    m "Well, whatever you're feeling, please know that it's completely valid and that you're not weak nor overemotional."
    m "And if you need to rant I'm always here to listen."
    m "I hope you get to feel more like yourself soon."
    m "Oh and [mas_get_player_nickname()], please know that I would never judge you for something you can't control."
    m "I love you so so much."
    m "Your girlfriend is here for you!"
    return "love"


init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="peMod_mood_cramps",
            prompt="...pain from cramps.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label peMod_mood_cramps:
    m "Oh no [player]!"
    m "I'm really sorry you're not feeling good right now."
    m "Is there anything I can do to help? Maybe let you rant about the pain or hold you?"
    m "I could also give you some tips to help with it as well!"
    m "I'm sorry, I'm panicking aren't I..."
    m "I just love you so much and I hate to see you in pain."
    m "Well anyway [mas_get_player_nickname()], I hope you start feeling better and maybe try running yourself a hot bath."
    m "Or putting your legs up and doing something you love."
    m "Please do take care of yourself."
    return "love"
