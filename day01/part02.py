from part01 import read_file, count_depth_increases


def determine_sliding_window(depths, size=3):
    result = []
    position = 0

    while position + size <= len(depths):
        window = 0
        for i in range(size):
            window += int(depths[position + i])

        result.append(window)
        position += 1

    return result


if __name__ == "__main__":
    print("STARTING PART 2")

    measurements = read_file("./measurements")
    measurements = determine_sliding_window(measurements)
    counter = count_depth_increases(measurements)

    print(f"END RESULT {counter}")
