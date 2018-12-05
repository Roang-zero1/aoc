def main():
    sum_escaped = 0
    sum_decoded = 0
    sum_double_encoded = 0
    with open('d8.txt') as input_file:
        for line in input_file.readlines():
            line = line.rstrip('\n')
            o_line = line
            sum_escaped += len(line)
            line = line[1:-1]
            line = bytes(line, "utf-8").decode("unicode_escape")
            sum_decoded += len(line)
            line = o_line
            line = line.replace('\"', '\\\"')
            line = line.replace('\\', '\\\\')
            line = line.replace('\\\"', '\"')
            sum_double_encoded += len(line) + 2

    print(f'The difference between escaped an decoded is {sum_escaped - sum_decoded}')
    print(f'The difference between escaped an double_escaped is {sum_double_encoded - sum_escaped}')

if __name__ == "__main__":
    main()
