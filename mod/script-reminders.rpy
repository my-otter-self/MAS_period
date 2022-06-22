# change pad/tampon reminder.

init 5 python in mas_bookmarks_derand:
    # Ensure things get bookmarked and derandomed as usual.
    label_prefix_map["peMod_change_reminder_"] = label_prefix_map["monika_"]


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_change_reminder_request",
            prompt="Can you remind me about changing my pads/tampons?",
            conditional="seen_event('peMod_topic_tss')",
            pool=True,
            action=EV_ACT_UNLOCK,
            rules={"no_unlock": None}
        )
    )

label peMod_change_reminder_request:
    m 7wub "[player], of course!"
    m 7wua "You know how worried I was when I researched about toxic shock syndrome..."
    m 3nublb "After all, your health and safety is my number one priority!"
    m 3wublb "So, [player], do you want to set a reminder?"

        m 4lubla "It's usually recommended to change your pads or tampons every 2 hours, is that okay with you?{nw}"
    menu:
        m "It's usually recommended to change your pads or tampons every 2 hours, is that okay with you?{fast}"

        "Yep!":
            $ interval = store.hyMod_reminder_utils.INTERVAL_HOURLY_2
            m 1dublb "Alrighty then! I'll be sure to remind you about it every two 2 hours, [mas_get_player_nickname()]~"
            m "When your period is over, you can ask me to stop reminding you!"
            m "Thank you for taking care of yourself, [player]~"
            jump .add_reminder

        "Maybe every 4 hours?":
            $ interval = store.hyMod_reminder_utils.INTERVAL_HOURLY_4

        "How about every 6 hours?":
            $ interval = store.hyMod_reminder_utils.INTERVAL_HOURLY_6

    m 1dublb "Alrighty then! I'll be sure to remind you about it every few hours, [mas_get_player_nickname()]~"

label .add_reminder:
    python:
        store.peMod_reminder.addRecurringReminder(
            "hyMod_reminder_event",
            datetime.timedelta(seconds=3600), interval, store.peMod_reminder_utils.LATENCY_HOURLY
        )

        mas_hideEVL("hyMod_reminder_start", "EVE", lock=True)
        mas_showEVL("hyMod_reminder_stop", "EVE", unlock=True)

    return "derandom"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="peMod_change_reminder_stop",
            prompt="You no longer need to remind me about changing pads/tampons.",
            category=["health"],
            pool=True,
            rules={"no_unlock": None}
        )
    )

label peMod_change_reminder_stop:
    m 7esb "Okay! I'll stop~"

    python:
        # Same here, DO NOT move this anywhere, this has to be right above the return statement.
        store.peMod_reminder.stopReminder("peMod_medication_reminder")

        # Hide this event as now we need to enable player to ask to remind again.
        mas_hideEVL("peMod_medication_reminder_stop", "EVE", lock=True)
        mas_showEVL("peMod_medication_reminder_request", "EVE", unlock=True)

    return


init 5 python:
    store.peMod_reminder.addReminderEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_medication_reminder",
            conditional="store.mshMod_reminder.shouldTriggerReminder('mshMod_medication_reminder')",
            action=EV_ACT_QUEUE,
            rules={"force repeat": None, "bookmark_rule": mas_bookmarks_derand.BLACKLIST}
        )
    )

label peMod_change_reminder:
    m 7esb "Hey, [player]!"
    m 1wsb "It's time to change your pad or tampons into a new one!"
    m 1ksb "Don't forget to carefully throw away the used one~"
    m 1hsbla "I love you!"

    # Do not move this anywhere, this must be above the return.
    $ store.peMod_reminder.extendCurrentReminder()
    return "love"
