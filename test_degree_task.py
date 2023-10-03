import pytest

from degree_task import degree


test_data = (
    ((10, 3, 5, 1), 34.39),
    ((15, 6, 2), 92.87),
    ((100, 200, 33, 15), 157.94),
)

@pytest.mark.parametrize('source, expected', test_data)
def test_degree(source: tuple[float], expected: float):
    assert degree(*source) == expected