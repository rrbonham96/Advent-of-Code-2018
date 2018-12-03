def get_id():
    input = []
    with open("input.txt") as infile:
        input = infile.readlines()
    input = list(map(lambda s: s.strip(), input))
    differences = 0
    for string1 in input:
        for string2 in input:
            for i in range(len(string1)):
                if string1[i] is not string2[i]:
                    differences += 1
            if differences is 1:
                return (string1, string2)
            differences = 0



if __name__ == '__main__':
    correct_id = get_id()
    print(correct_id)
