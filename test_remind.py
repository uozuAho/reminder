from datetime import datetime
from io import StringIO
import pytest

import remind

def test_add_reminder():
    file = StringIO()
    now = datetime(2024, 6, 15, 12)
    remind.add_reminder(file, now, "eat chicken at 5pm")
    file.seek(0)
    text = file.read()
    assert text == "2024-06-15 17:00: eat chicken"

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
