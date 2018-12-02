


def parse_frequency():
    strings = []
    with open("frequency_input.txt") as infile:
        strings = infile.readlines()
    inputs = [int(x) for x in strings]
    frequency = 0
    for number in inputs:
        frequency += number
    return frequency


if __name__ == '__main__':
    frequency = parse_frequency()
    print(frequency)
