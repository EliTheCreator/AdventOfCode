from string import ascii_lowercase


def main():
    with open("input", "r") as file:
        steps = file.readline().split(",")

    boxes = [[] for _ in range(256)]
    for step in steps:
        box_number = 0
        lens_name = ""
        for index, symbol in enumerate(step):
            if symbol in ascii_lowercase:
                lens_name += symbol
                box_number += ord(symbol)
                box_number *= 17
            else:
                break

        box_number %= 256

        match step[len(lens_name)]:
            case '-':
                for index, (name, _) in enumerate(boxes[box_number]):
                    if lens_name == name:
                        boxes[box_number].pop(index)
                        break
            case '=':
                focal_length = int(step[len(lens_name)+1])
                for index, (name, _) in enumerate(boxes[box_number]):
                    if lens_name == name:
                        boxes[box_number][index] = (lens_name, focal_length)
                        break
                else:
                    boxes[box_number].append((lens_name, focal_length))
            case _:
                exit(-1)

    focusing_power = 0
    for box_number, box in enumerate(boxes, 1):
        for slot_number, (_, focal_length) in enumerate(box, 1):
            focusing_power += box_number*slot_number*focal_length

    print(focusing_power)


if __name__ == "__main__":
    main()
