import sys
import os
sys.path.append(os.path.abspath("../intcode_computer"))
from intcode_computer import IntcodeComputer


def get_code():
    with open("input.txt") as f:
        input_str = f.read()

    code = input_str.split(',')
    code = [int(x) for x in code]

    return code


def part_one():
    code = get_code()
    computer = IntcodeComputer()
    computer.set_input(1)
    computer.execute_program(code)


def part_two():
    code = get_code()
    computer = IntcodeComputer()
    computer.set_input(5)
    computer.execute_program(code)


part_one()
part_two()
