def get_range():
    with open("input.txt") as f:
        split = f.read().split('-')
        return int(split[0]), int(split[1])


def calculate_next_password(password_str,
                            last_increasing_digit_index,
                            last_increasing_digit_str):
    new_password = list(password_str)
    for j in range(last_increasing_digit_index, len(new_password)):
        new_password[j] = str(last_increasing_digit_str)
    return int("".join(new_password))


def is_password_meeting_criteria(password, require_separated=False):
    double_occurred = False
    current_double_group = None
    double_groups_separated = []

    password_str = str(password)
    previous_digit = int(password_str[0])
    for i in range(1, len(password_str)):
        digit = int(password_str[i])
        if previous_digit > digit:
            return calculate_next_password(password_str, i, previous_digit)

        if previous_digit == digit:
            double_occurred = True
            if current_double_group and digit == current_double_group:
                if digit in double_groups_separated:
                    double_groups_separated.remove(digit)
            else:
                double_groups_separated.append(digit)
            current_double_group = digit
        else:
            current_double_group = None

        previous_digit = digit

    if require_separated:
        return double_occurred and len(double_groups_separated) > 0

    return double_occurred


def count_passwords(require_separated):
    start, end = get_range()

    ok_passwords = 0
    i = start
    while i <= end:
        result = int(is_password_meeting_criteria(i, require_separated))
        if result == 1:
            ok_passwords += 1
            i += 1
        elif result > 1:
            i = result
        else:
            i += 1

    print(ok_passwords)


def part_one():
    count_passwords(False)


def part_two():
    count_passwords(True)


part_one()
part_two()
