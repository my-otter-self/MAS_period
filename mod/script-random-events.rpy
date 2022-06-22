#random period dialogues

# Ensure things get bookmarked and derandomed as usual.
init 5 python in mas_bookmarks_derand:
    label_prefix_map["peMod_topic_"] = label_prefix_map["monika_"]

#intro, sets variable
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_intro",
            category=["health"],
            prompt="[player] and periods",
            random=True
        )
    )

label peMod_topic_intro:
    m "[player], I've been thinking and I now feel comfortable of discussing something with you."
    m "It's something completely natural, something that I experience and you might, too."
    m "It's menstruation, or like many people call it, periods!"
    m "You know, I get those like everyone else..."
    m "And I wanted to ask, do you experience periods?{nw}"
    $ _history_list.pop()
    menu:
        m "And I wanted to ask, do you experience periods?{fast}"

        "Yes, I do!":
        #set variable period=true here
            m "Oh, I see!"
            m "Another thing we have in common, ehehe~"
            m "I hope you don't get too inconvenienced by it."
            m "Periods can make us so uncomfortable!"
            m "But it's how our bodies work..."
            m "I'll try to give you some tips ans information about it, [player]!"
            m "Knowledge is never too much."
            m "Thanks for trusting in me!"

        "No, I don't.":
        #set variable period=false here
            m "Oh, I see! "
            extend "Do you want to hear a little about it then?"

            m "I can talk to you about how it works, and give you new information on the topic.{nw}"
            menu:
                m "I can talk to you about how it works, and give you new information on the topic.{fast}"

                "Yes!":
                #set variable so all the other dialogues show
                    m "Yay!"
                    m "So, you know..."
                    #add dialogue here

                "No, let's not talk about it.":
                #set variable so other dialogues dont show
                    m "Oh, I see! I'm sorry..."
                    m "I won't bring up this topic again."

        "I don't want to talk about it.":
        #set variable so other dialogues dont show
            m "Oh, I see! I'm sorry..."
            m "But that's okay, [player]. Your privacy is super important!"
            m "I won't bring up this topic again."

    return

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
    m "It's really dangerous and so many people don't know about it..."
    m "But it has other risk factors! Such as open skin wounds and surgery."

    #if period=false
    m "So be careful anyway, [player]!"
    m "I worry and care for you."
    m "I love you!"

    #if period=true
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
    m "The human body works in mysterious ways."

    #if period=false
    m "Thank you for listening and for being okay with me talking about this, [player]!"
    m "I love you~"

    #if period=true
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
            prompt="Pre Menstrual Syndrome",
            random=True
        )
    )

label peMod_topic_pms:
    m "[player], do you know about pre menstrual symdrome?"
    m "A myriad of people who experience periods suffer from it!"
    m "In case you don't know, pre menstrual syndrome, commonly known as PMS..."
    m "Is a time where those who have periods will get irritable, anxious, and overall more hormonal before their period."
    m "However, the symptoms can be physical as well!"

    #if period=false
    m "If you're close to someone that experiences PMS, make sure to be supportive during those days."
    m "They might not be feeling like themselves at the moment."
    m "Thanks for listening, [player]!"

    #if period=true
    m "[mas_get_player_nickname(capitalize=True)], if you have post menstrual symptoms, you can rant to me about it anytime."
    m "I'll understand! "
    extend "And I'll hope you'll get to feel more like yourself later."
    m "I love you~"
    return "love"
