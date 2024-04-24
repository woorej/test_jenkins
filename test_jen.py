from jen import add_numbers
import pytest

@pytest.mark.parametrize("n1, n2, expected_result",[
    (2, 3, 5),
    (4, 5, 9),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add_numbers(n1, n2, expected_result):
    assert add_numbers(n1, n2) == expected_result

