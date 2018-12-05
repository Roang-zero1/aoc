with open("d1.txt") as input_file:
    position = 0
    for line in input_file.readlines():
        position += int(line)
    print(f"End position: {position}")
		