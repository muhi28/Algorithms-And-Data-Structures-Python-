import random


# initializes the list with random numbers
def getData(n):
    arr = [0] * n

    for i in range(n):
        arr[i] = random.randint(1, 100)

    return arr


# sorts the data based on the selection sort algorithm
def selectionSort(arr):
    # search for the largest number
    # saves it in the maximum spot and then repeats searching through the array

    for fill_slot in range(len(arr) - 1, 0, -1):
        max_pos = 0

        for location in range(1, fill_slot + 1):

            if arr[location] > arr[max_pos]:
                max_pos = location

        swap(arr, fill_slot, max_pos)
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
