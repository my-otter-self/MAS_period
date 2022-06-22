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
    m "Oh no, [player]!"
    #add dialogue
    return


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
    m "[player]!"
    #add dialogue
    return
