
def main():
    with open("input", "r") as file:
        numbers = [int(x) for x in file.readline().strip()]

    full_blocks = [(num_blocks, file_index) for file_index, num_blocks in enumerate(numbers[::2])]
    empty_blocks = numbers[1::2]

    disk = []
    prev_empty_idx = -1
    empty_idx = prev_empty_idx+1
    prev_full_idx = len(full_blocks)
    full_idx = prev_full_idx-1
    while empty_idx < full_idx:
        if prev_empty_idx != empty_idx:
            disk.append(full_blocks[empty_idx])
        prev_empty_idx = empty_idx
        prev_full_idx = full_idx

        num_empty_blocks = empty_blocks[empty_idx]
        num_full_blocks, file_idx = full_blocks[full_idx]
        if num_empty_blocks > num_full_blocks:
            disk.append((num_full_blocks, file_idx))
            full_idx -= 1
            empty_blocks[empty_idx] = num_empty_blocks-num_full_blocks
        elif num_empty_blocks == num_full_blocks:
            disk.append((num_full_blocks, file_idx))
            empty_idx += 1
            full_idx -= 1
        else:
            disk.append((num_empty_blocks, file_idx))
            empty_idx += 1
            full_blocks[full_idx] = (num_full_blocks-num_empty_blocks, file_idx)

    if prev_empty_idx != empty_idx and prev_full_idx == full_idx:
        disk.append(full_blocks[full_idx])

    total = 0
    index = 0
    for num_blocks, file_idx in disk:
        for _ in range(num_blocks):
            total += index*file_idx
            index += 1

    print(total)


if __name__ == "__main__":
    main()
