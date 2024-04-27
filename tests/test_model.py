import pytest

from src.pytemplate.domain.model import Operand


def test_operands_immutable():
    operands = Operand(5, 10)
    with pytest.raises(AttributeError):
        operands.first_operand = 15
    with pytest.raises(AttributeError):
        operands.second_operand = 20


def test_operands_values():
    operands = Operand(5, 10)
    assert isinstance(operands.first_operand, int)
    assert isinstance(operands.second_operand, int)
