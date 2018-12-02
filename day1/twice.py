def get_twice():
    strings = []
    with open("frequency_input.txt") as infile:
        strings = infile.readlines()
    inputs = [int(x) for x in strings]
    frequency_set = set()
    frequency = 0
    frequency_set.add(frequency)
    found_twice = False
    while not found_twice:
        for number in inputs:
            frequency += number
            if frequency in frequency_set:
                twice = frequency
                found_twice = True
                break
            else:
                frequency_set.add(frequency)
    return twice


if __name__ == '__main__':
    twice = get_twice()
    print(twice)
