import random

"""
Example of Bubble Sort Algorithm
"""

# initializes the list with random numbers
def getData(n):
    data = [0] * n

    for i in range(n):
        data[i] = random.randint(1, 100)

    return data


# Sorts the data based on the BubbleSort-Algorithm
def bubbleSort(data):
    for i in range(len(data) - 1, 0, -1):

        for j in range(i):

            if data[j] > data[j + 1]:
                # used to swap data
                data[j], data[j + 1] = data[j + 1], data[j]


# used to show the data within the console
def printData(data):
    for i in range(len(data)):
        print("Number {0:d} -> {1:d}".format(i, data[i]))


def main():
    data = getData(10)

    print("Before Sorting -> {0:}".format(data))

    bubbleSort(data)

    print("After Sorting -> {0:}".format(data))


if __name__ == '__main__':
    main()
