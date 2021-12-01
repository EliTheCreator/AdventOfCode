
def main():
    with open("input", "r") as file:
        mes = [int(x) for x in file.readlines()]

    ### First Version ###
    # sums = [x + y + z for ((x, y), z)
    #         in zip(zip(mes[2:], mes[1:-1]), mes[:-2])]

    # print(len([True for (x, y) in zip(sums[:-1], sums[1:]) if x < y]))

    ### Simplified Version ###
    # This works because:
    #       (mes[i] + mes[i+1] + mes[i+2]) < (mes[i+1] + mes[i+2] + mes[i+3])
    #   ==  mes[i] < mes[i+3]
    print(len([True for (x, y) in zip(mes[:-3], mes[3:]) if x < y]))


if __name__ == "__main__":
    main()
