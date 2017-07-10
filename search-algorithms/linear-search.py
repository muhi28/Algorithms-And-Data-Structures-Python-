import random


# initializes the list with random numbers
def getData(n):
    arr = [0] * n

    for i in range(n):
        arr[i] = random.randint(1, 100)

    return arr


def linearSearch(arr, value):
    for i in range(0, len(arr)):
        if arr[i] == value:
            return "True | Index -> {0:d}".format(i)

    return "False | Index -> null"


def main():
    data_size = input("How many elements do you want to insert?\t")
    data = getData(data_size)
    print "Data -> {0:}".format(data)

    # search for random number between 1 and 100
    print "Found value -> {0:s}\n".format(linearSearch(data, random.randint(1, 100)))

    # search for fixed number
    data = [4, 80, 47, 55, 10, 5, 6, 8, 1, 1, 2, 698]
    print "Data -> {0:}".format(data)
    print "Found value -> {0:s}".format(linearSearch(data, 2))


if __name__ == '__main__':
    main()
