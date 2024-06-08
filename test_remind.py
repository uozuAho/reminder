import pytest

import remind

testdata = [
    ("do thing at 5", "at 5"),
    ("do thing at 5pm", "at 5pm"),
]

@pytest.mark.parametrize("text, expected", testdata)
def test_get_time_phrase(text, expected):
    assert remind.get_time_phrase(text) == expected
