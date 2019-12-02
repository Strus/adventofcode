import math


def get_mass_list():
    with open("input.txt") as f:
        input_str = f.read()

    mass_list = input_str.split('\n')
    mass_list = [float(x) for x in mass_list]
    return mass_list


def part_one():
    mass_list = get_mass_list()
    mass_list = [math.floor(x/3) - 2 for x in mass_list]
    print(sum(mass_list))


def calculate_fuel_needed(mass):
    fuel_needed = math.floor(mass/3) - 2
    if fuel_needed <= 0:
        return 0

    fuel_needed += calculate_fuel_needed(fuel_needed)
    return fuel_needed


def part_two():
    mass_list = get_mass_list()
    mass_list = [calculate_fuel_needed(x) for x in mass_list]
    print(sum(mass_list))


part_one()
part_two()
