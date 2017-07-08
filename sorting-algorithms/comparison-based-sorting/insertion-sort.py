import random

"""
Insertion Sort Algorithm
"""


# initializes the list with random numbers
def getData(n):
    data = [0] * n

    for i in range(n):
        data[i] = random.randint(1, 100)

    return data


# used to show the data within the console
def printData(data):
    for i in range(len(data)):
        print "Number {0:d} -> {1:d}".format(i, data[i])


# sorts the given data based on the insertion sort algorithm
def insertionSort(data):
    for i in range(1, len(data)):
        numb = data[i]
        j = i

        while j > 0 and (data[j - 1] > numb):
            data[j] = data[j - 1]
            j -= 1

        data[j] = numb


def main():
    data_size = input("How many elements do you want to insert?\t")

    data = getData(data_size)

    print "\nBefore Sorting -> {0:}".format(data)

    insertionSort(data)

    print "After Sorting with Insertion Sort -> {0:}".format(data)


if __name__ == '__main__':
    main()
