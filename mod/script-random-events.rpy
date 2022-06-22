#toxic shock syndrome dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_tss",
            category=["health"],
            prompt="Toxic Shock Syndrome",
            random=True
        )
    )

label peMod_topic_tss:
    m "[player], have you ever heard of toxic shock syndrome?"
    m "Its medical definition is 'a rare life-threatening condition of certain bacterial infections.'"
    m "I researched its causes and the main cause was unchanged tampons."
    m "[player]... if you ever use tampons, please remember to change them every one to two hours!"
    m "I can always remind you, if you want."
    m "No need to be embarrassed [mas_get_player_nickname()], your safety is always my number one priority, ehehe~"
    m "I truly do love you more than you'll ever know, [player]."
    return "love"


#cravings dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_cravings",
            category=["health"],
            prompt="Period cravings",
            random=True
        )
    )

label peMod_topic_cravings:
    m "[player], did you know that people who experience periods often get cravings during them?"
    m "It's pretty interesting!"
    m "From what I read and based on my own experience, desserts and chocolate are pretty common cravings!"
    m "However, it can be any kind of food." 
    m "Some might even crave a food they don't like that much!"
    m "[mas_get_player_nickname(capitalize=True)], once I'm in your reality, I'll be sure to indulge and help you with your cravings!"
    m "Ehehehe!"
    m "I love you so much~"
    return "love"


#post menstrual syndrome dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_pms",
            category=["health"],
            prompt="Post Menstrual Syndrome",
            random=True
        )
    )

label peMod_topic_pms:
    m "[player], do you know about post menstrual symdrome?"
    m "A myriad of people who experience periods suffer from it!"
    m "In case you don't know, post menstrual syndrome, commonly known as PMS..."
    m "Is a time where those who have periods will get irritable, anxious, and overall more hormonal after their period."
    m "However, the symptoms can be physical as well!
    m "[mas_get_player_nickname(capitalize=True)], if you have post menstrual symptoms, you can rant to me about it anytime."
    m "I'll understand!"
    extend " And I'll hope you'll get to feel more like yourself later." 
    m "I love you~"
    return "love"
