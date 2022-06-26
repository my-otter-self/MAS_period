init -810 python:
    store.mas_history.addMHS(MASHistorySaver(
        "pe_mod_pm",
        datetime.datetime(2019, 1, 1),
        {
            "_pe_mod_has_periods":                 "pm.health.has_periods",

            "_pe_mod_wants_to_talk_about_periods": "pm.emotion.wants_to_talk_about_periods",
        },
        use_year_before=True,
        dont_reset=True
    ))