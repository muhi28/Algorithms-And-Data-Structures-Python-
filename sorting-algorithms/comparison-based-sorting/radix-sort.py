import random

"""
Radix Sort Example
"""


# initializes the list with random numbers
def getData(n):
    arr = [0] * n

    for i in range(n):
        arr[i] = random.randint(1, 100)

    return arr


# used to do counting sort of data[] according
# to the given digit (exp)
def countSort(arr, n, exp):
    # array that will have the sorted data
    output = [0] * n

    count = [0] * 10

    # stores count of occurrences in count[]
    for i in range(0, n):
        idx = (arr[i] / exp)
        count[idx % 10] += 1

    # used to change count[i] so that it now contains
    # the actual position of this digit in output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # builds the output data
    i = n - 1

    while i >= 0:
        idx = (arr[i] / exp)
        output[count[idx % 10] - 1] = arr[i]
        count[idx % 10] -= 1
        i -= 1

    for j in range(0, len(arr)):
        arr[j] = output[j]


# Radix Sort algorithm
def radixSort(arr):
    # searches for the max numb to know the number of digits
    mx = max(arr)

    # do counting sort for every digit
    exp = 1

    while mx / exp > 0:
        countSort(arr, len(arr), exp)
        exp *= 10


class RadixSort:
    def __init__(self):
        pass


if __name__ == '__main__':
    data_size = input("How many elements do you want to insert?\t")
    data = getData(data_size)
    print "Data before Sorting -> {0:}".format(data)
    radixSort(data)
    print "Data after Sorting -> {0:}".format(data)
