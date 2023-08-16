from hey import hey

def test_default():
    assert hey() == "hey, world"

def test_argument():
    assert hey("Mansi") == "hey, Mansi"