# My terminal reminder app

# usage
python remind.py [args]

# dev quick start
```sh
# setup
python -m venv .venv
. .venv/bin/activate
pip install pip-tools
pip-compile
pip-sync

# test
pytest
```

# todo
```sh
remind all                  # DONE: show all reminders
remind <message plus time>  # add a reminder
remind                      # show all due reminders
remind snz <id> <time>      # 'snooze' a reminder until time
                            # reminder id: hash of the message?
remind snz [time]           # snooze most overdue reminder
```

time phrases:
- DONE at 5pm
- DONE in 1 hour(s), minutes
- tomorrow
- in Xday(s),week(s)
- on friday
- next week
- this weekend
