from datetime import datetime
from pathlib import Path
import pytest

import remind


TEST_INFILE = Path('test_data/reminders.txt')
TEST_OUTFILE = Path('test_output/reminders.txt')


def test_add_reminder():
    now = datetime(2024, 6, 15, 12)
    run("eat chicken at 5pm", now)
    result = default_output()
    result_lines = result.splitlines()
    assert len(result_lines) == 3  # appends to the end
    assert result_lines[2] == "2024-06-15 17:00: eat chicken"


def test_add_reminder_appends_line():
    now = datetime(2024, 6, 15, 12)
    run("eat chicken at 5pm", now)
    # do 2 in case original file already has a newline:
    run("eat chicken at 5pm", now, infile=TEST_OUTFILE)
    result = default_output()
    result_lines = result.splitlines()
    assert len(result_lines) == 4


time_phrases = [
    ("do thing at 5", "at 5"),
    ("do thing at 5pm", "at 5pm"),
    ("do thing in 1 hour", "in 1 hour"),
    ("do thing tomorrow", "tomorrow"),
]

@pytest.mark.parametrize("text, expected", time_phrases)
def test_get_time_phrase(text, expected):
    assert remind.get_time_phrase(text) == expected


time_of_cases = [
    (datetime(2024, 6, 8, 8, 0, 0),  "at 9", datetime(2024, 6, 8, 9, 0 ,0)),
    (datetime(2024, 6, 8, 8, 0, 0),  "at 9pm", datetime(2024, 6, 8, 21, 0 ,0)),
    (datetime(2024, 6, 8, 10, 0, 0), "at 9", datetime(2024, 6, 8, 21, 0 ,0)),
    (datetime(2024, 6, 8, 12, 0, 0), "at 5", datetime(2024, 6, 8, 17, 0 ,0)),
    (datetime(2024, 6, 8, 12, 0, 0), "at 5pm", datetime(2024, 6, 8, 17, 0 ,0)),
    (datetime(2024, 6, 8, 12, 0, 0), "in 20 minutes", datetime(2024, 6, 8, 12, 20 ,0)),
    (datetime(2024, 6, 8, 12, 0, 0), "in 1 hour", datetime(2024, 6, 8, 13, 0 ,0)),
    (datetime(2024, 6, 8, 12, 0, 0), "in 2 hours", datetime(2024, 6, 8, 14, 0 ,0)),
    (datetime(2024, 6, 8, 12, 0, 0), "tomorrow", datetime(2024, 6, 9, 8, 0 ,0))
]

@pytest.mark.parametrize("time_now, phrase, expected", time_of_cases)
def test_time_of(time_now, phrase, expected):
    assert remind.time_of(time_now, phrase) == expected


def run(text: str,
        now: datetime,
        infile = TEST_INFILE,
        outfile = TEST_OUTFILE):
    remind.run(infile, outfile, now, text.split())


def default_output():
    with open(TEST_OUTFILE) as file:
        return file.read()
