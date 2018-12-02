def get_checksum():
    input = []
    with open("input.txt") as infile:
        input = infile.readlines()

    chars = dict()
    for char in "abcdefghijklmnopqrstuvwxyz":
        chars[char] = 0

    twos = 0
    threes = 0

    input = list(map(lambda s: s.strip(), input))

    for id in input:
        for char in id:
            chars[char] += 1
        if 2 in chars.values():
            twos += 1
        if 3 in chars.values():
            threes += 1
        for key in chars.keys():
            chars[key] = 0
    return twos * threes


if __name__ == '__main__':
    checksum = get_checksum()
    print(checksum)
