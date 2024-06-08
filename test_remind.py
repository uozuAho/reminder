from datetime import datetime
import pytest

import remind

time_phrases = [
    ("do thing at 5", "at 5"),
    ("do thing at 5pm", "at 5pm"),
]

@pytest.mark.parametrize("text, expected", time_phrases)
def test_get_time_phrase(text, expected):
    assert remind.get_time_phrase(text) == expected


time_of_cases = [
    (datetime(2024, 6, 8, 12, 0, 0), "at 5", datetime(2024, 6, 8, 17, 0 ,0))
]

@pytest.mark.parametrize("time_now, phrase, expected", time_of_cases)
def test_time_of(time_now, phrase, expected):
    assert remind.time_of(time_now, phrase) == expected
