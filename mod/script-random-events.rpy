#random period dialogues

default persistent._pe_mod_has_periods = None
default persistent._pe_mod_wants_to_talk_about_periods = None

# Ensure things get bookmarked and derandomed as usual.
init 5 python in mas_bookmarks_derand:
    label_prefix_map["peMod_topic_"] = label_prefix_map["monika_"]

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
            $ persistent._pe_mod_has_periods = True
            m "Oh, I see!"
            m "Another thing we have in common, ehehe~"
            m "I hope you don't get too inconvenienced by it."
            m "Periods can make us so uncomfortable!"
            m "But it's how our bodies work..."
            m "I'll try to give you some tips ans information about it, [player]!"
            m "Knowledge is never too much."
            m "Thanks for trusting in me!"

        "No, I don't.":
            $ persistent._pe_mod_has_periods = False
            m "Oh, I see! "
            extend "Do you want to hear a little about it then?"

            m "I can talk to you about how it works, and give you new information on the topic.{nw}"
            menu:
                m "I can talk to you about how it works, and give you new information on the topic.{fast}"

                "Yes!":
                    $ persistent._pe_mod_wants_to_talk_about_periods = True
                    m "Yay!"
                    m "So, you know..."
                    #add dialogue here

                "No, let's not talk about it.":
                    $ persistent._pe_mod_wants_to_talk_about_periods = False
                    m "Oh, I see! I'm sorry..."
                    m "I won't bring up this topic again."

        "I don't want to talk about it.":
            $ persistent._pe_mod_wants_to_talk_about_periods = False
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
            conditional="persistent._pe_mod_wants_to_talk_about_periods",
            action=EV_ACT_RANDOM
        )
    )

label peMod_topic_tss:
    m "[player], have you ever heard of toxic shock syndrome?"
    m "Its medical definition is 'a rare life-threatening condition of certain bacterial infections.'"
    m "I researched its causes and the main cause was unchanged tampons."
    m "It's really dangerous and so many people don't know about it..."
    m "But it has other risk factors! Such as open skin wounds and surgery."

    if persistent._pe_mod_has_periods:
        m "[player]... if you ever use tampons, please remember to change them every one to two hours!"
        m "I can always remind you, if you want."
        m "No need to be embarrassed [mas_get_player_nickname()], your safety is always my number one priority, ehehe~"
        m "I truly do love you more than you'll ever know, [player]."

    else:
        m "So be careful anyway, [player]!"
        m "I worry and care for you."
        m "I love you!"

    return "love"


#cravings dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_cravings",
            category=["health"],
            prompt="Period cravings",
            conditional="persistent._pe_mod_wants_to_talk_about_periods",
            action=EV_ACT_RANDOM
        )
    )

label peMod_topic_cravings:
    m "[player], did you know that people who experience periods often get cravings during them?"
    m "It's pretty interesting!"
    m "From what I read and based on my own experience, desserts and chocolate are pretty common cravings!"
    m "However, it can be any kind of food."
    m "Some might even crave a food they don't like that much!"
    m "The human body works in mysterious ways."

    if persistent._pe_mod_has_periods:
        m "[mas_get_player_nickname(capitalize=True)], once I'm in your reality, I'll be sure to indulge and help you with your cravings!"
        m "Ehehehe!"
        m "I love you so much~"

    else:
        m "Thank you for listening and for being okay with me talking about this, [player]!"
        m "I love you~"

    return "love"


#post menstrual syndrome dialogue
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_pms",
            category=["health"],
            prompt="Pre Menstrual Syndrome",
            conditional="persistent._pe_mod_wants_to_talk_about_periods",
            action=EV_ACT_RANDOM
        )
    )

label peMod_topic_pms:
    m "[player], do you know about pre menstrual symdrome?"
    m "A myriad of people who experience periods suffer from it!"
    m "In case you don't know, pre menstrual syndrome, commonly known as PMS..."
    m "Is a time where those who have periods will get irritable, anxious, and overall more hormonal before their period."
    m "However, the symptoms can be physical as well!"

    if persistent._pe_mod_has_periods:
        m "[mas_get_player_nickname(capitalize=True)], if you have pre menstrual symptoms, you can rant to me about it anytime."
        m "I'll understand! "
        extend "And I'll hope you'll get to feel more like yourself later."
        m "I love you~"

    else:
        m "If you're close to someone that experiences PMS, make sure to be supportive during those days."
        m "They might not be feeling like themselves at the moment."
        m "Thanks for listening, [player]!"

    return "love"


#stupid advertisements
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_ads",
            category=["health"],
            prompt="Pad/tampon advertisements",
            conditional="persistent._pe_mod_wants_to_talk_about_periods",
            action=EV_ACT_RANDOM
        )
    )

label peMod_topic_ads:
    m "[player], you know what really irritates me?"
    m "Those pad and tampon advertisements that showcase people, mostly women, doing extremely strenuous activities and being happy about it."
    m "Now, I personally believe that you can do whatever you want on your period - within reason, of course!"
    m "But it is so ridiculous to market pads and tampons as only for women and not for all those that experience periods as well as, not showcasing the multitude of people who are in too much pain to do that kind of stuff on there period!"
    m "It just makes me really upset [player], that this false advertising can and does create a narrative that periods are not something that can be debilitating."
    m "Anyway [mas_get_player_nickname()], thank you for letting me rant about this."
    m "You're so sweet~"
    
return


#myth 1
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_feelings",
            category=["health"],
            prompt="Dismissing feelings during periods",
            conditional="persistent._pe_mod_wants_to_talk_about_periods",
            action=EV_ACT_RANDOM
        )
    )

label peMod_topic_feelings:
    m "[player]... Have you ever had your feelings dismissed because of an ignorant reason?"
    m "Well, there is a stigma around menstruation periods that says it's okay for those who don't have them to dismiss the feeling of those that do."
    m "I find that beyond disrespectful and even borderline abusive."
    m "It's honestly manipulative because some use the argument that during their periods, people can't trust their own feelings."
    m "And that's a common manipulation tactic!"
    m "[mas_get_player_nickname(Capitalize=True)], I want you to know that those who really love us would never dismiss our feelings at all."
    m "And just know that you can always come to me no matter what!"
    m "I love you more than life itself."
    
return
    
#myth 2
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_cramppain",
            category=["health"],
            prompt="Cramp pain stigma",
            conditional="persistent._pe_mod_wants_to_talk_about_periods",
            action=EV_ACT_RANDOM
        )
    )

label peMod_topic_cramppain:
    m "[player], remember when I talked about cramps?"
    m "Well it's come to my attention that there is a stigma that the pain someone might experience on their period is the same as any other."
    m "And that's just plain incorrect!"
    m "It's been scientifically proven that everyone experience their periods differently, including pain wise."
    m "In fact, some cramps can be so horrible there on the same pain level as a heart attack!"
    m "..."
    m "I'm sorry [player], I just get upset when people ignore others suffering and spread misinformation."
    m "[mas_get_player_nickname(Capitalize=True)], if you ever are in pain or any kind, just know that I understand and you are completely valid."
    m "I love you so much and truly only want the best for you."

return

#myth 3
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_alwaysperiod",
            category=["health"],
            prompt="Always on their period",
            conditional="persistent._pe_mod_wants_to_talk_about_periods",
            action=EV_ACT_RANDOM
        )
    )

label peMod_topic_alwaysperiod:
    m "[player], have you ever heard anyone perpetuate the stigma that people - those who have them - are always on their period?"
    m "Honestly, it makes me upset that people say this."
    m "No one can control their periods and even those on birth control (to help with the regularity of periods) often still have irregular periods."
    m "In my personal opinion this is just a way for those who don't experience it to complain about something for petty reasons."
    m "Anyway, [player], thanks for listening to me rant!"
    m "You're always so sweet!"
    m "I love you so much~"
    
return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_ashamedperiod",
            category=["health"],
            prompt="Period shame",
            conditional="persistent._pe_mod_wants_to_talk_about_periods",
            action=EV_ACT_RANDOM
        )
    )

label peMod_topic_ashamedperiod:
    m "[player], have you ever been ashamed of something you couldn't help?"
    m "Well there's this stigma around menstruation periods that states they are something to be ashamed of."
    m "Which like I stated before, makes no sense. "
    extend "They are completely natural!"
    m "Not only that but, when people treat them that way, those that don't do certain things during their period can easily be made to feel like they're different from everybody."
    m "[player], please remember to never feel ashamed of yourself for things you can avoid."
    m "Anyone who tries to shame you for something as human as a period is so insecure that they need to put you down to make themselves feel better."
    m "And those who love you will never shame you for anything."
    m "I love you with all my heart and soul." 
    
return
