import random


# initializes the list with random numbers
def getData(n):
    arr = [0] * n

    for i in range(n):
        arr[i] = random.randint(1, 100)

    return arr


def binarySearch(arr, value):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) / 2

        if arr[mid] == value:

            return "True | Index -> {0:d}".format(mid)

        elif value < arr[mid]:

            last = mid - 1

        else:
            first = mid + 1

    return "False | Index -> null"


def main():
    data_size = input("How many elements do you want to insert?\t")
    data = getData(data_size)
    print "Data -> {0:}".format(data)

    # search for random number between 1 and 100
    print "Found value -> {0:s}\n".format(binarySearch(data, random.randint(1, 100)))

    # search for fixed number
    data = [2, 4, 8, 20, 30, 80, 140, 857, 900]
    print "Data -> {0:}".format(data)
    print "Found value -> {0:s}".format(binarySearch(data, 900))


if __name__ == '__main__':
    main()
