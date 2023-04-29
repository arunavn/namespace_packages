# Third party imports
import pytest

# from my_caculator imports
from my_calculator import operations


def test_operations_add_them():
    assert operations.add_them() > 0
