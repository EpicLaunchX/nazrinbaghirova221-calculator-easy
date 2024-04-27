from dataclasses import dataclass


@dataclass(frozen=True)
class Operand:
    first_operand: int
    second_operand: int
