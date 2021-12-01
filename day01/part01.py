def read_file(file_name):
    print(f"READING FILE {file_name}")
    with open(file_name) as file:
        content = file.readlines()

    return content


def count_depth_increases(depth_list):
    counter = 0
    prev_measurement = int(depth_list[0])

    for line in depth_list[1:]:
        measurement = int(line)

        if measurement > prev_measurement:
            counter += 1
        prev_measurement = measurement

    return counter


if __name__ == "__main__":
    print("STARTING PART 1")

    measurements = read_file("./measurements")
    counter = count_depth_increases(measurements)

    print(f"END RESULT {counter}")
