from datetime import datetime, timedelta
import sys
import re


def main():
    _, reminders_file, *args = sys.argv
    if args == ['all']:
        with open(reminders_file) as file:
            for line in file.readlines():
                print(line.strip())
    else:
        pass


def get_time_phrase(str: str):
    a = re.findall(r'at \d+.*$', str)
    if a: return a[-1]
    a = re.findall(r'in \d+.*$', str)
    if a: return a[-1]
    if str.endswith('tomorrow'): return 'tomorrow'
    raise Exception("no time phrase found")


def time_of(time_now: datetime, phrase: str) -> datetime:
    if phrase.startswith('at'):
        return time_at(time_now, phrase)
    elif phrase.startswith('in'):
        return time_in(time_now, phrase)
    elif phrase.endswith('tomorrow'):
        return time_tomorrow(time_now)
    raise Exception("I dunno")


def time_in(time_now, phrase):
    m = re.match(r'[^\d]*(\d+)\s*(.*)', phrase)
    number = int(m.group(1))
    units = m.group(2).strip()
    if 'min' in units:
        return time_now + timedelta(minutes=number)
    if 'hour' in units:
        return time_now + timedelta(hours=number)
    raise Exception(f'invalid unit {units}')


def time_at(time_now: datetime, phrase: str) -> datetime:
    m = re.match(r'.*(\d)(.*)', phrase)
    hour = int(m.group(1))
    ampm = m.group(2)
    if ampm == 'pm':
        hour += 12
    if not ampm:
        if time_now.hour > hour:
            hour += 12
    return datetime(
        time_now.year,
        time_now.month,
        time_now.day,
        hour
    )


def time_tomorrow(time_now: datetime):
    start_of_day = 8
    tomorrow = time_now + timedelta(days=1)
    return datetime(
        tomorrow.year,
        tomorrow.month,
        tomorrow.day,
        start_of_day
    )


if __name__ == '__main__':
    main()
