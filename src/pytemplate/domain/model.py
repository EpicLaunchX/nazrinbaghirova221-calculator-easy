from dataclasses import dataclass


@dataclass(frozen=True)
class Operands:
    first_operand: int
    second_operand: int
