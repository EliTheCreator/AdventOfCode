
def main():
    with open("input", "r") as file:
        numbers = [int(x) for x in file.readline().strip()]

    full_blocks = [(num_blocks, file_index) for file_index, num_blocks in enumerate(numbers[::2])]
    empty_blocks = numbers[1::2] + [0]

    new_blocks = [[] for _ in empty_blocks]
    for full_idx, (num_blocks, file_index) in reversed(list(enumerate(full_blocks))):
        for empty_idx, empty_len in enumerate(empty_blocks[:full_idx]):
            if num_blocks <= empty_len:
                new_blocks[empty_idx].append((num_blocks, file_index))
                full_blocks[full_idx] = (0, 0)
                empty_blocks[empty_idx] -= num_blocks
                empty_blocks[full_idx-1] += num_blocks
                break

    total = 0
    index = 0
    for full, new, empty in zip(full_blocks, new_blocks, empty_blocks):
        for (num_blocks, file_idx) in [full]+new:
            for _ in range(num_blocks):
                total += index*file_idx
                index += 1
        index += empty

    print(total)


if __name__ == "__main__":
    main()
