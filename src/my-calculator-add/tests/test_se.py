# Third party imports
import pytest

# from my_caculator imports
from my_calculator.basic import add


def test_operations_add_them():
    assert add.add(1,3) == 4
