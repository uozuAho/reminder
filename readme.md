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

# add alias
. remind.sh

# commands
remind                      # show due reminders
remind all                  # show all reminders
```

# todo
- WIP: remind rm <substring>       # remove reminder matching substr (only 1)
    - removes one
    - throws on multi match
    - warns when nothing done
- print a confirmation eg "I'll remind you: '' at {}", "reminder deleted: {}"
```sh
remind <message plus time>  # add a reminder
remind snz <id> <time>      # 'snooze' a reminder until time
                            # reminder id: hash of the message?
remind snz [time]           # snooze most overdue reminder
```
- add `remind` to bashrc
- time phrases:
    - DONE at 5pm
    - DONE in 1 hour(s), minutes
    - DONE tomorrow
    - in Xday(s),week(s)
    - on friday
    - next week
    - this weekend

- maybe: cron + broadcast?
- maybe: email?
