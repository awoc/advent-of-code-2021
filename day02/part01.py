def determine_position(measurements):
    x = 0
    y = 0

    for line in measurements:
        splited_string = line.split()
        command = splited_string[0]
        value = int(splited_string[1])

        if command == "forward":
            x += value
        elif command == "up":
            y -= value
        elif command == "down":
            y += value

    return (x, y)


if __name__ == "__main__":
    with open("./input.txt") as file:
        content = file.readlines()

    x, y = determine_position(content)

    print(f"Result {x} * {y} = {x * y}")
