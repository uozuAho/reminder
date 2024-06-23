from datetime import datetime, timedelta
from io import TextIOWrapper
from pathlib import Path
import sys
import re
import typing as t


def main():
    _, reminders_file, *args = sys.argv
    run(reminders_file, reminders_file, datetime.now(), args)


def run(infile: Path, outfile: Path, now: datetime, args: t.List[str]):
    output_text = ''
    if outfile != infile:
        with open(infile) as ifile:
            with open(outfile, 'w') as ofile:
                intext = ifile.read()
                ofile.write(intext)
                if not intext.endswith('\n'):
                    ofile.writelines([''])
    if args == ['all']:
        with open(infile) as file:
            for line in file.readlines():
                output_text += line.strip() + '\n'
    elif len(args) > 0:
        with open(outfile, 'a') as file:
            add_reminder(file, now, ' '.join(args))
    else:
        # no args
        for due, msg in get_due_reminders(infile, now):
            output_text += f'{due.strftime("%Y-%m-%d %H:%M")}: {msg}'
    print(output_text)
    return output_text


def add_reminder(reminders_file: TextIOWrapper, now: datetime, text: str):
    time_phrase = get_time_phrase(text)
    reminder_text = text.split(time_phrase)[0].strip()
    reminder_time = time_of(now, time_phrase)
    reminders_file.write(f'{reminder_time.strftime("%Y-%m-%d %H:%M")}: {reminder_text}\n')


def get_due_reminders(file: Path, now: datetime) -> t.Iterable[t.Tuple[datetime, str]]:
    with open(file) as infile:
        for line in infile:
            due, message = read_reminder(line)
            if now > due:
                yield due, message


def read_reminder(line: str):
    date_str = line[:16]
    due = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    return due, line[18:].strip()


def get_time_phrase(str: str):
    a = re.findall(r'at \d+.*$', str)
    if a:
        return a[-1]
    a = re.findall(r'in \d+.*$', str)
    if a:
        return a[-1]
    if str.endswith('tomorrow'):
        return 'tomorrow'
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
    if not m:
        raise Exception("could not match time_at")
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
