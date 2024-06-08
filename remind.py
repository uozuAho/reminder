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
    a = re.search(r'at \d+')
    if a: return a


if __name__ == '__main__':
    main()
