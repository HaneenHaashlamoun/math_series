from math_series import __version__
from math_series.series import fibonacci

def test_version():
    assert __version__ == '0.1.0'


def test_fib():
    expected = 8
    actual = fibonacci(6)
    assert actual == expected




