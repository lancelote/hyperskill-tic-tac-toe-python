from src.stage3.hw1 import get_running_sum


def test_get_running_sum():
    assert get_running_sum("15325") == [1, 6, 9, 11, 16]
