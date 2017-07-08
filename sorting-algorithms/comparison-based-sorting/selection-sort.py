import random


# initializes the list with random numbers
def getData(n):
    arr = [0] * n

    for i in range(n):
        arr[i] = random.randint(1, 100)

    return arr


# sorts the data based on the selection sort algorithm
def selectionSort(arr):
    # search for the smallest number
    # saves it in the minimum spot and then repeats searching through the array
    for i in range(0, len(arr)):
        minimum = i
        for j in range(i, len(arr)):

            if arr[minimum] > arr[j]:
                minimum = j

        swap(arr, i, minimum)

    return arr


def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def main():
    data_size = input("How many elements do you want to insert?\t")
    data = getData(data_size)
    print "Data before Sorting -> {0:}".format(data)

    print "Data after Sorting -> {0:}".format(selectionSort(data))


if __name__ == '__main__':
    main()
