from datetime import datetime
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


def get_time_phrase(str):
    a = re.findall(r'at \d+.*$', str)[-1]
    if a: return a


def time_of(time_now: datetime, phrase: str) -> datetime:
    if phrase.startswith('at'):
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
    return datetime.now()


if __name__ == '__main__':
    main()
