import pytest


@pytest.mark.parametrize("x1, y1, x2, y2, input_x, expected", [
    (2, 1, 8, 2, 6, 1.6666666666666667),
    (2, 1, 8, 2, 12, 2.666666666666667),
])
def test_calculate_y(x1, y1, x2, y2, input_x, expected):
    from point_on_slope import calculate_y
    answer = calculate_y(x1, y1, x2, y2, input_x)
    assert answer == expected
