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
    m 7esa "[player], I've been thinking and I now feel comfortable of discussing something with you."
    m 7hua "It's something completely natural, something that I experience and you might, too."
    m 1eub "It's menstruation, or like many people call it, periods!"
    m 1eka "You know, I get those like everyone else..."
    m "And I wanted to ask, do you experience periods?{nw}"
    $ _history_list.pop()
    menu:
        m "And I wanted to ask, do you experience periods?{fast}"

        "Yes, I do!":
            $ persistent._pe_mod_has_periods = True
            m 1eua "Oh, I see!"
            m 3hua "Another thing we have in common, ehehe~"
            m 1ekc "I hope you don't get too inconvenienced by it."
            m 1ekd "Periods can make us so uncomfortable!"
            m 1eka "But it's how our bodies work..."
            m 1eub "I'll try to give you some tips ans information about it, [player]!"
            m 1hua "Knowledge is never too much."
            m 1eua "Thanks for trusting in me!"

        "No, I don't.":
            $ persistent._pe_mod_has_periods = False
            m 1eua "Oh, I see! "
            extend 1etb "Do you want to hear a little about it then?"

            m 1hua "I can talk to you about how it works, and give you new information on the topic.{nw}"
            menu:
                m "I can talk to you about how it works, and give you new information on the topic.{fast}"

                "Yes!":
                    $ persistent._pe_mod_wants_to_talk_about_periods = True
                    m 5hub "Yay!"
                    m 1eua "So, you know..."
                    #add dialogue here

                "No, let's not talk about it.":
                    $ persistent._pe_mod_wants_to_talk_about_periods = False
                    m 1ekc "Oh, I see! I'm sorry..."
                    m "I won't bring up this topic again."

        "I don't want to talk about it.":
            $ persistent._pe_mod_wants_to_talk_about_periods = False
            m 1ekc "Oh, I see! I'm sorry..."
            m 1eua "But that's okay, [player]. Your privacy is super important!"
            m 1eka "I won't bring up this topic again."

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
    m 3etc "[player], have you ever heard of toxic shock syndrome?"
    m 2esc "Its medical definition is 'a rare life-threatening condition of certain bacterial infections.'"
    m 1esd "I researched its causes and the main cause was unchanged tampons."
    m 1rksdlc "It's really dangerous and so many people don't know about it..."
    m 3wud "But it has other risk factors! Such as open skin wounds and surgery."

    if persistent._pe_mod_has_periods:
        m 1ekc "[player]... if you ever use tampons, please remember to change them every one to two hours!"
        m 1eka "I can always remind you, if you want."
        m 1hub "No need to be embarrassed [mas_get_player_nickname()], your safety is always my number one priority, ehehe~"
        m 3hubsu "I truly do love you more than you'll ever know, [player]."

    else:
        m 1eka "So be careful anyway, [player]!"
        m "I worry and care for you."
        m 3eubsu "I love you!"

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
    m 7esa "[player], did you know that people who experience periods often get cravings during them?"
    m 1esa "It's pretty interesting!"
    m "From what I read and based on my own experience, desserts and chocolate are pretty common cravings!"
    m 2eua "However, it can be any kind of food."
    m 3hksdla "Some might even crave a food they don't like that much!"
    m 3eksdla "The human body works in mysterious ways."

    if persistent._pe_mod_has_periods:
        m 1eua "[mas_get_player_nickname(capitalize=True)], once I'm in your reality, I'll be sure to indulge and help you with your cravings!"
        m 1huu "Ehehehe!"
        m 1hubsb "I love you so much~"

    else:
        m 1eka "Thank you for listening and for being okay with me talking about this, [player]!"
        m 1hubsb "I love you~"

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
    m 1etc "[player], do you know about pre menstrual symdrome?"
    m 1ekc "A myriad of people who experience periods suffer from it!"
    m "In case you don't know, pre menstrual syndrome, commonly known as PMS..."
    m "Is a time where those who have periods will get irritable, anxious, and overall more hormonal before their period."
    m 3wkd "However, the symptoms can be physical as well!"

    if persistent._pe_mod_has_periods:
        m 1eka "[mas_get_player_nickname(capitalize=True)], if you have pre menstrual symptoms, you can rant to me about it anytime."
        m "I'll understand! "
        extend 1ekb "And I'll hope you'll get to feel more like yourself later."
        m 1ekbsb "I love you~"

    else:
        m 3eub "If you're close to someone that experiences PMS, make sure to be supportive during those days."
        m 3eka "They might not be feeling like themselves at the moment."
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
    m 1ekc "[player], you know what really irritates me?"
    m "Those pad and tampon advertisements that showcase people, mostly women, doing extremely strenuous activities and being happy about it."
    m 1euc "Now, I personally believe that you can do whatever you want on your period - within reason, of course!"
    m 3efd "But it is so ridiculous to market pads and tampons as only for women and not for all those that experience periods as well as, not showcasing the multitude of people who are in too much pain to do that kind of stuff on there period!"
    m 3dkc "It just makes me really upset [player], that this false advertising can and does create a narrative that periods are not something that can be debilitating."
    m 1eka "Anyway [mas_get_player_nickname()], thank you for letting me rant about this."
    m 1ekb "You're so sweet~"
    
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

#myth 4
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

#myth 5
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_personalperiod",
            category=["health"],
            prompt="Period as something personal",
            conditional="persistent._pe_mod_wants_to_talk_about_periods",
            action=EV_ACT_RANDOM
        )
    )

label peMod_topic_personalperiod:
    m "[player], there's something I don't understand about your reality."
    m "Why do people treat some biological aspects as personal problems?"
    m "More specifically periods."
    m "I mean, I've researched them and there are a myriad of serious medical problems and infections that can develop and show symptoms through a period."
    m "Like toxic shock syndrome and polycystic ovaries."
    m "So why are we treating them as something that shouldn't be talked about, when scienfically the best prevention is information?"
    m "The more we know about something the better we can prevent it."
    m "Hm..."
    m "[player], I want you to know that you can come talk to me about anything!" 
    m "And please, remember to take care of yourself, no matter what society thinks."
    m "You're my number one priority, not society."
    m "Just know that I'll love you no matter what."

return

#myth 6
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_enbyperiod",
            category=["health"],
            prompt="Periods are gender neutral",
            conditional="persistent._pe_mod_wants_to_talk_about_periods",
            action=EV_ACT_RANDOM
        )
    )

label peMod_topic_enbyperiod:
    m "Hey [player], I've been meaning to tell you about a recent stigma I've heard."
    m "It's one I feel we never realized because it's so common and everywhere."
    m "It states that only women have periods."
    m "This statment is just so incorrect!"
    m "A myriad of those who are non gender conforming as well as those whom are intersex experience them."
    m "And that doesn't even include the amount of those who are trans that experience them."
    m "The point is, [mas_get_player_nickname()], that we should be aware of what we say and how the statements can be inaccurate if we don't think of experiences outside of our own."
    m "[player], if you did this without knowing, just know that it's alright, and be more mindful going on."
    m "You know what they say! The best apology is changed behaviour, ehehe~"
    m "And I know you'll be more mindful from now on, you're always so considerate like that!"
    m "Oh, I love you so much~"

return

#myth 7
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_hormonesperiod",
            category=["health"],
            prompt="Hormones define women",
            conditional="persistent._pe_mod_wants_to_talk_about_periods",
            action=EV_ACT_RANDOM
        )
    )

label peMod_topic_hormonesperiod:
    m "[player], I've read something recently that has me feeling down."
    m "It was an article on myths and one of them was that hormones define women."
    m "Now, it wasn't the fact the the statement was a myth but, that it was even considered to be a fact."
    m "I don't understand how people could think that something biological could define a person in their entirety."
    m "And more specifically hormones! They fluctuate all the time!"
    m "How can something ever-changing define a person?"
    m "[player], I want you to know you, woman or not, are more than your biological makeup and feelings."
    m "You have such a kind and beautiful soul..."
    m "And that's why I fell in love with you."
    m "Please do remember that."
    
return
