from itertools import accumulate, cycle


def get_frequencies_list():
    with open("input.txt") as f:
        freq_txt = f.read()

    freq_list = freq_txt.split('\n')
    freq_list = [int(x) for x in freq_list]
    return freq_list


def part_one():
    freq_list = get_frequencies_list()
    print(sum(freq_list))


def part_two():
    freq_list = get_frequencies_list()
    seen = {0}
    for freq in accumulate(cycle(freq_list)):
        if freq in seen:
            print(freq)
            return

        seen.add(freq)


part_one()
part_two()

