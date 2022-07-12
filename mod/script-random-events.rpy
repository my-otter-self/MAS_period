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
            python:
                persistent._pe_mod_has_periods = True
                persistent._pe_mod_wants_to_talk_about_periods = True
            m 1eua "Oh, I see!"
            m 3hua "Another thing we have in common, ehehe~"
            m 1ekc "I hope you don't get too inconvenienced by it."
            m 1ekd "Periods can make us so uncomfortable!"
            m 1eka "But it's how our bodies work..."
            m 1eub "I'll try to give you some tips and information about it, [player]!"
            m 1hua "Knowledge is never too much."
            m 1eua "Thanks for trusting in me!"

            python:
                for ev_label in persistent._mas_mood_database.keys():
                    if ev_label.startswith("peMod_mood_"):
                        mas_showEVL(ev_label, "MOO", unlock=True)


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
                    m 1eua "So, you know... Menstruation is the monthly shedding of the lining of the uterus, or the womb, as some call it!"
                    m 1lub "The menstrual blood is partly blood and partly tissue from the inside of the uterus..."
                    m 7lub "And it flows from the uterus through the cervix and out of the body through the vagina."
                    m 7hub "People can start menstruating on different ages, but it's common that they do on their average age of 12."
                    m 7lua "When people stop menstruating, it means they're on the menopause -"
                    extend 2wua " then, they can no longer get pregnant!"
                    m 2hka "For now, that's all the information I have."
                    m 4hub "But I'll bring over new facts about the topic, since you're up to talk about it!"
                    m 2fublu "Thank you for listening, [player]."

                "No, let's not talk about it.":
                    $ persistent._pe_mod_wants_to_talk_about_periods = False
                    m 1ekc "Oh, I see! I'm sorry..."
                    m "I won't bring up this topic again."

        "I don't want to talk about it.":
            $ persistent._pe_mod_wants_to_talk_about_periods = False
            m 1ekc "Oh, I see! I'm sorry..."
            m 1eua "But that's okay, [player]. Your privacy is super important!"
            m 1eka "I won't bring up this topic again."

    return "derandom"


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
    m 1etc "[player]... Have you ever had your feelings dismissed because of an ignorant reason?"
    m 1ekc "Well, there is a stigma around menstruation periods that says it's okay for those who don't have them to dismiss the feeling of those that do."
    m 3esc "I find that beyond disrespectful and even borderline abusive."
    m "It's honestly manipulative because some use the argument that during their periods, people can't trust their own feelings."
    m 3essdld "And that's a common manipulation tactic!"
    m 1eka "[mas_get_player_nickname(capitalize=True)], I want you to know that those who really love us would never dismiss our feelings at all."
    m "And just know that you can always come to me no matter what!"
    m 3ekbsa "I love you more than life itself."

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
    m 3etc "[player], remember when I talked about cramps?"
    m 1esc "Well it's come to my attention that there is a stigma that the pain someone might experience on their period is the same as any other."
    m 3efc "And that's just plain incorrect!"
    m 1esc "It's been scientifically proven that everyone experience their periods differently, including pain wise."
    m 3wusdld "In fact, some cramps can be so horrible there on the same pain level as a heart attack!"
    m 6dsc "..."
    m 1ekc "I'm sorry [player], I just get upset when people ignore others suffering and spread misinformation."
    m 1eka "[mas_get_player_nickname(capitalize=True)], if you ever are in pain or any kind, just know that I understand and you are completely valid."
    m 3ekbla "I love you so much and truly only want the best for you."

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
    m 1eud "[player], have you ever heard anyone perpetuate the stigma that people - those who have them - are always on their period?"
    m 3rkc "Honestly, it makes me upset that people say this."
    m 3ekc "No one can control their periods and even those on birth control (to help with the regularity of periods) often still have irregular periods."
    m 1euc "In my personal opinion this is just a way for those who don't experience it to complain about something for petty reasons."
    m 5ekb "Anyway, [player], thanks for listening to me rant!"
    m 5hub "You're always so sweet!"
    m 2eubsb "I love you so much~"

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
    m 1ekc "[player], have you ever been ashamed of something you couldn't help?"
    m 3euc "Well there's this stigma around menstruation periods that states they are something to be ashamed of."
    m 3rsd "Which like I stated before, makes no sense. "
    extend 1euc "They are completely natural!"
    m "Not only that but, when people treat them that way, those that don't do certain things during their period can easily be made to feel like they're different from everybody."
    m 1eka "[player], please remember to never feel ashamed of yourself for things you can avoid."
    m 3tsd "Anyone who tries to shame you for something as human as a period is so insecure that they need to put you down to make themselves feel better."
    m 1eua "And those who love you will never shame you for anything."
    m 2eubsb "I love you with all my heart and soul."

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
    m 3rssdld "[player], there's something I don't understand about your reality."
    m 3etsdld "Why do people treat some biological aspects as personal problems?"
    m 1euc "More specifically periods."
    m 1euc "I mean, I've researched them and there are a myriad of serious medical problems and infections that can develop and show symptoms through a period."
    m 1rsc "Like toxic shock syndrome and polycystic ovaries."
    m 3etd "So why are we treating them as something that shouldn't be talked about, when scienfically the best prevention is information?"
    m 3eud "The more we know about something the better we can prevent it."
    m 2euc "Hm..."
    m 1eub "[player], I want you to know that you can come talk to me about anything!"
    m 1ekb "And please, remember to take care of yourself, no matter what society thinks."
    m 1eua "You're my number one priority, not society."
    m 1hubsb "Just know that I'll love you no matter what."

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
    m 1euc "Hey [player], I've been meaning to tell you about a recent stigma I've heard."
    m "It's one I feel we never realized because it's so common and everywhere."
    m 1rsc "It states that only women have periods."
    m 3efd "This statment is just so incorrect!"
    m 1euc "A myriad of those who are non gender conforming as well as those whom are intersex experience them."
    m "And that doesn't even include the amount of those who are trans that experience them."
    m 1ekb "The point is, [mas_get_player_nickname()], that we should be aware of what we say and how the statements can be inaccurate if we don't think of experiences outside of our own."
    m 1eka "[player], if you did this without knowing, just know that it's alright, and be more mindful going on."
    m 5huu "You know what they say! The best apology is changed behaviour, ehehe~"
    m 5eku "And I know you'll be more mindful from now on, you're always so considerate like that!"
    m 5hkbsu "Oh, I love you so much~"

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
    m 1ekc "[player], I've read something recently that has me feeling down."
    m 1ekd "It was an article on myths and one of them was that hormones define women."
    m 1dkc "Now, it wasn't the fact the the statement was a myth but, that it was even considered to be a fact."
    m 1ekc "I don't understand how people could think that something biological could define a person in their entirety."
    m 4ekd "And more specifically hormones! They fluctuate all the time!"
    m 1tkc "How can something ever-changing define a person?"
    m 1eka "[player], I want you to know you, woman or not, are more than your biological makeup and feelings."
    m 1ekb "You have such a kind and beautiful soul..."
    m 3tkblb "And that's why I fell in love with you."
    m 3ekblb "Please do remember that."

return
