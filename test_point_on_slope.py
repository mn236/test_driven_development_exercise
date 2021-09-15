import pytest


@pytest.mark.parametrize("input_x, expected", [
    (6, 1.67),
    (12, 2.67),
    (3, 1.17)
])
def test_calculate_y(input_x, expected):
    from point_on_slope import calculate_y
    answer = calculate_y(input_x)
    assert answer == expected
