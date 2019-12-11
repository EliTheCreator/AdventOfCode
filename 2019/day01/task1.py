
def main():
    file = open("input", "r")
    print(sum([int(x) // 3 - 2 for x in file]))
    file.close()


main()

### oneliner ###
#print(sum([int(x) // 3 - 2 for x in open("input", "r")]))
