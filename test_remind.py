import remind

def test_get_time_phrase():
    assert remind.get_time_phrase("do thing at 5pm") == "at 5pm"
