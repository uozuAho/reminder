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
        number = int(re.findall(r'\d+$', phrase)[0])
        return datetime(
            time_now.year,
            time_now.month,
            time_now.day,
            12 + number
        )
    return datetime.now()


if __name__ == '__main__':
    main()
