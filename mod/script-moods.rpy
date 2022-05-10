init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mpm_mood_bad",
            prompt="...bad.",
            category=[store.mas_moods.TYPE_BAD],
            unlocked=True
        ),
        code="MOO"
    )

label mpm_mood_bad:
    pass
