import random

"""
Quick-Sort example with pivot on different positions
"""


# creates a switch statement
class Switch(object):
    value = None

    def __new__(cls, value):
        cls.value = value
        return True


# initializes the list with random numbers
def getData(n):
    data = [0] * n

    for i in range(n):
        data[i] = random.randint(1, 100)

    return data


# Sorts the data based on the QuickSort-Algorithm
def quicksort(data, left, right, mode):
    pivot = checkForPivot(data, left, right, mode)

    i = left
    j = right

    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1

        if i <= j:
            swap(data, i, j)

            i += 1
            j -= 1

    if left < j:
        quicksort(data, left, j, mode)
    if i < right:
        quicksort(data, i, right, mode)


# used to swap data
def swap(data, i, j):
    z = data[i]
    data[i] = data[j]
    data[j] = z


# prints the data within the console
def printData(data):
    for i in range(len(data)):
        print "Number {0:d} -> {1:d}".format(i, data[i])


def checkForPivot(data, left, right, mode):
    while Switch(mode):

        # pivot on right side
        if case(1):
            return data[right]

        # median of five
        if case(2):
            data2 = [data[left], data[int(left + ((right - left) / 4))], data[int(left + ((right - left) / 2))],
                     data[int(right - ((right - left) / 4))], data[right]]

            quicksort(data2, 0, len(data2) - 1, 1)
            return data2[2]


# determines whether our switch statement contains the specified value
def case(*args):
    return any((arg == Switch.value for arg in args))


# used to start the main function
def main():
    data_size = input("How many elements do you want to insert?\t")

    # ---------------------- pivot on right side ----------------------
    data = getData(data_size)

    print "\nBefore Sorting -> {0:}".format(data)

    quicksort(data, 0, len(data) - 1, 1)
    print "After Sorting with QuickSort (pivot on right side) -> {0:}\n\n".format(data)

    # ---------------------- median of five ---------------------
    data = getData(data_size)
    print "Before Sorting -> {0:}".format(data)

    quicksort(data, 0, len(data) - 1, 2)
    print "After Sorting with QuickSort (median of five) -> {0:}\n".format(data)


if __name__ == '__main__':
    main()
