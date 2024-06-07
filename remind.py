import sys


def main():
    _, reminders_file, *args = sys.argv
    # print(reminders_file)
    # print(args)
    if not args:
        with open(reminders_file) as file:
            for line in file.readlines():
                print(line.strip())


if __name__ == '__main__':
    main()
