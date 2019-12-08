class IntcodeInstruction:
    def __init__(self, raw_instruction="0"):
        self.parameter_modes = [0, 0, 0]

        raw_instruction_length = len(raw_instruction)
        if raw_instruction_length <= 2:
            self.opcode = int(raw_instruction)
        elif raw_instruction_length == 3:
            self.opcode = int(raw_instruction[-2:])
            self.parameter_modes[0] = int(raw_instruction[0])
        elif raw_instruction_length == 4:
            self.opcode = int(raw_instruction[-2:])
            self.parameter_modes[0] = int(raw_instruction[1])
            self.parameter_modes[1] = int(raw_instruction[0])
        elif raw_instruction_length == 5:
            self.opcode = int(raw_instruction[-2:])
            self.parameter_modes[0] = int(raw_instruction[2])
            self.parameter_modes[1] = int(raw_instruction[1])
            self.parameter_modes[2] = int(raw_instruction[0])


class IntcodeComputer:
    def __init__(self):
        self.instruction_pointer = 0
        self.input = None

    def set_input(self, input_val):
        self.input = input_val

    def get_parameters_positions(self, instruction, code):
        if instruction.parameter_modes[0] == 0:
            first_position = code[self.instruction_pointer + 1]
        else:
            first_position = self.instruction_pointer + 1

        if instruction.parameter_modes[1] == 0:
            second_position = code[self.instruction_pointer + 2]
        else:
            second_position = self.instruction_pointer + 2

        if instruction.parameter_modes[2] == 0:
            result_position = code[self.instruction_pointer + 3]
        else:
            result_position = self.instruction_pointer + 3

        return first_position, second_position, result_position

    def add(self, instruction, code):
        first_position, second_position, result_position \
            = self.get_parameters_positions(instruction, code)

        code[result_position] = \
            code[first_position] + code[second_position]

        self.instruction_pointer += 4

    def multiply(self, instruction, code):
        first_position, second_position, result_position \
            = self.get_parameters_positions(instruction, code)

        code[result_position] = \
            code[first_position] * code[second_position]

        self.instruction_pointer += 4

    def store_input(self, instruction, code):
        result_position, _, _ \
            = self.get_parameters_positions(instruction, code)

        code[result_position] = self.input

        self.instruction_pointer += 2

    def output_val(self, instruction, code):
        result_position, _, _ \
            = self.get_parameters_positions(instruction, code)

        print("# " + str(code[result_position]))

        self.instruction_pointer += 2

    def jump_if_true(self, instruction, code):
        first_position, result_position, _ \
            = self.get_parameters_positions(instruction, code)

        if code[first_position] > 0:
            self.instruction_pointer = code[result_position]
        else:
            self.instruction_pointer += 3

    def jump_if_false(self, instruction, code):
        first_position, result_position, _ \
            = self.get_parameters_positions(instruction, code)

        if code[first_position] == 0:
            self.instruction_pointer = code[result_position]
        else:
            self.instruction_pointer += 3

    def less_than(self, instruction, code):
        first_position, second_position, result_position \
            = self.get_parameters_positions(instruction, code)

        code[result_position] = 1 if code[first_position] < code[second_position] else 0
        self.instruction_pointer += 4

    def equals(self, instruction, code):
        first_position, second_position, result_position \
            = self.get_parameters_positions(instruction, code)

        code[result_position] = 1 if code[first_position] == code[second_position] else 0
        self.instruction_pointer += 4

    def execute_program(self, code):
        self.instruction_pointer = 0
        instruction = IntcodeInstruction()
        while instruction.opcode != 99:
            instruction = IntcodeInstruction(str(code[self.instruction_pointer]))
            if instruction.opcode == 1:
                self.add(instruction, code)
            elif instruction.opcode == 2:
                self.multiply(instruction, code)
            elif instruction.opcode == 3:
                self.store_input(instruction, code)
            elif instruction.opcode == 4:
                self.output_val(instruction, code)
            elif instruction.opcode == 5:
                self.jump_if_true(instruction, code)
            elif instruction.opcode == 6:
                self.jump_if_false(instruction, code)
            elif instruction.opcode == 7:
                self.less_than(instruction, code)
            elif instruction.opcode == 8:
                self.equals(instruction, code)

        print("END")
