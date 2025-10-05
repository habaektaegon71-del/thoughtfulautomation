import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from func import sort

@pytest.mark.parametrize(
	"width, height, length, mass, expected",
	[
		(10, 100, 100, 10, "STANDARD"),
		(100, 100, 100, 10, "SPECIAL"), # Equal to 1000000 cm^3. Bulky, but not heavy
		(1000,1000,1000, 10, "SPECIAL"), # Greater than 1000000 cm^3
		(10, 10, 10, 50, "SPECIAL"), # Heavy, but not bulky
		(1, 150, 1, 10, "SPECIAL"), # Heavy, but not bulky
		(1000,1000,1000, 50, "REJECTED"), # Heavy and bulky
	]
)
def test_sort(width, height, length, mass, expected):
	assert sort(width, height, length, mass) == expected
