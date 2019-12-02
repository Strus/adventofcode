def get_instructions_list(noun, verb):
    with open("input.txt") as f:
        input_str = f.read()

    instructions = input_str.split(',')
    instructions = [int(x) for x in instructions]
    instructions[1] = noun
    instructions[2] = verb

    return instructions


def add(instructions, address):
    first_position = instructions[address + 1]
    second_position = instructions[address + 2]
    result_position = instructions[address + 3]

    instructions[result_position] = \
        instructions[first_position] + instructions[second_position]


def multiply(instructions, address):
    first_position = instructions[address + 1]
    second_position = instructions[address + 2]
    result_position = instructions[address + 3]

    instructions[result_position] = \
        instructions[first_position] * instructions[second_position]


def execute_program(instructions):
    instruction_pointer = 0
    while instructions[instruction_pointer] != 99:
        if instructions[instruction_pointer] == 1:
            add(instructions, instruction_pointer)
        elif instructions[instruction_pointer] == 2:
            multiply(instructions, instruction_pointer)
        instruction_pointer += 4


def part_one():
    instructions = get_instructions_list(12, 2)
    execute_program(instructions)
    print(instructions[0])


def find_noun_verb_pair():
    for noun in range(100):
        for verb in range(100):
            instructions = get_instructions_list(noun, verb)
            execute_program(instructions)
            if instructions[0] == 19690720:
                return noun, verb


def part_two():
    noun, verb = find_noun_verb_pair()
    print(100 * noun + verb)


part_one()
part_two()
