from hello import add


def test_hello():

    assert add(5, 6) == 11
    assert add(4, 6) == 10
    assert add(4, 5) != 0
