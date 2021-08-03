from hello import add


def test_hello():

    assert add(5, 6) == 6
    assert add(4, 6) ==6
    assert add(4, 5) != 0
