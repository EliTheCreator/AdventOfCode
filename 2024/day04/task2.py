
def main():
    with open("input", "r") as file:
        word_search = ["." + line.strip() + "." for line in file.readlines()]
        word_search = ["."*len(word_search[0])] + word_search + ["."*len(word_search[0])]

    x_mas_count = 0
    for row in range(1, len(word_search)-1):
        for col in range(1, len(word_search[0])-1):
            if word_search[row][col] != 'A':
                continue

            ms = 0
            mrow = 0
            mcol = 0
            ss = 0
            for drow, dcol in ((-1,-1), (-1,1), (1,-1), (1,1)):
                match word_search[row+drow][col+dcol]:
                    case 'M':
                        ms += 1
                        mrow += drow
                        mcol += dcol
                    case 'S':
                        ss += 1
                    case _:
                        break

            x_mas_count += ms==2 and ss==2 and (mrow!=0 or mcol!=0)

    print(x_mas_count)


if __name__ == "__main__":
    main()
