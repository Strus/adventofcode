import sys
import os
sys.path.append(os.path.abspath("../intcode_computer"))
from intcode_computer import IntcodeComputer


def get_code(noun, verb):
    with open("input.txt") as f:
        input_str = f.read()

    code = input_str.split(',')
    code = [int(x) for x in code]
    code[1] = noun
    code[2] = verb

    return code


def part_one():
    code = get_code(12, 2)
    computer = IntcodeComputer()
    computer.execute_program(code)
    print(code[0])


def find_noun_verb_pair():
    for noun in range(100):
        for verb in range(100):
            code = get_code(noun, verb)
            computer = IntcodeComputer()
            computer.execute_program(code)
            if code[0] == 19690720:
                return noun, verb


def part_two():
    noun, verb = find_noun_verb_pair()
    print(100 * noun + verb)


part_one()
part_two()
