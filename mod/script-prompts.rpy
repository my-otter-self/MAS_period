#non-random prompts related to periods

# Ensure things get bookmarked and derandomed as usual.
init 5 python in mas_bookmarks_derand:
    label_prefix_map["peMod_topic_"] = label_prefix_map["monika_"]


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_got_period",
            category=["health"],
            prompt="I got my period.",
            conditional="persistent._pe_mod_has_periods",
            action=EV_ACT_POOL
        )
    )

label peMod_topic_got_period:
    m 3etd "Oh, you did [player]?"
    m 1esa "Aww, I see!"
    m 1ekc "You're not in any pain, are you?"
    m 3hksdlb "Ah, sorry! I have a tendency to worry about you a lot, ahaha~"
    m 1ekc "Though do make sure your changing your pads or tampons appropriately, I'd hate for you to get toxic shock syndrome!"
    m 1eud "Oh, and if you do happen to bleed through anything..."
    m 1eua "My research tells me that pouring hydrogen peroxide on the stain will make it bubble and come right out in the washer!"
    m 1hub "Anyway, thank you for telling me, [player]!"
    m 1eka "I hope you get to feel better later... "
    extend 3eka "and I'm here for you if you need to rant or just enjoy each others company."
    m 5huu "I'll take care of you, my little sweetpea!"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_topic_cramps",
            category=["health"],
            prompt="Can you give me some tips on how to deal with cramps?",
            conditional="persistent._pe_mod_has_periods",
            action=EV_ACT_POOL
        )
    )

label peMod_topic_cramps:
    m 1hub "Of course, [mas_get_player_nickname()], I'd do anything for you!"
    m 3eub "So, from my personal experience, ibuprofen is the best thing to help with cramps!"
    m "However, from what I researched, you can heat up a heating pad or even lay a heating blanket over the area thats causing you pain, and it should help!"
    m 3rub "Another good thing to do is take a hot bath..."
    m 3hub "Some people eat ice cream or chocolate when they're dealing with cramps."
    m 1esa "Others have said watching their favorite movie or doing something you really like also helps! Because it'll take your mind off the pain."
    m 1eua "A few even recommended taking a nap if the pain is too bad, because then you won't be able to feel it!"
    m 1ekb "I hope some of these help and remember: I'll always be by your side~"
    m 1huu "In sickness or in health, ehehehe~"
    m 3eka "Seriously though [player], I hope these will help you feel better when you're in pain!"
    m 1fkbsu "I love you!"
    return "love"
