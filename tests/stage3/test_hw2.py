from src.stage3.hw2 import running


def test_running():
    assert running("12345") == [1.5, 2.5, 3.5, 4.5]
