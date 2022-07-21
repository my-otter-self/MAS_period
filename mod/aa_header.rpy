init -990 python in mas_submod_utils:
    Submod(
        author="MAS Period Mod Team",
        name="MAS Period Mod",
        description="information about menstruating, and an opportunity for players to tell monika they're on their period and topics related",
        version="1.0.0"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MAS Period Mod",
            user_name="my-otter-self",
            repository_name="mas_period",
            submod_dir="/Submods/MAS Period Mod",
            extraction_depth=3,
            redirected_files=(
                "readme.md",
                "license.txt"
            )
        )

init 10 python:
    if mas_seenLabels(["peMod_change_reminder_start"]):
        # Manually unlock as a bugfix
        if store.peMod_reminder.isReminderActive('peMod_change_reminder'):
            # Hide start and show stop if reminder is active
            mas_hideEVL("peMod_change_reminder_start", "EVE", lock=True)
            mas_showEVL("peMod_change_reminder_stop", "EVE", unlock=True)
        else:
            # Hide stop and show start if reminder is not active
            mas_hideEVL("peMod_medication_reminder_stop", "EVE", lock=True)
            mas_showEVL("peMod_medication_reminder_start", "EVE", unlock=True)