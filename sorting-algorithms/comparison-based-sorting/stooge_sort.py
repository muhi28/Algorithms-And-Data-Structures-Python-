import random


# initializes the list with random numbers
def getData(n):
    data = [0] * n

    for i in range(n):
        data[i] = random.randint(1, 100)

    return data


def stoogeSort(arr, i, j):
    # checks whether the value at the start is larger
    # then the value at the end
    if arr[j] < arr[i]:
        # if it's so -> swap them
        arr[i], arr[j] = arr[j], arr[i]

    # if there are 3 or more elements
    if (j - i + 1) >= 3:
        t = (j - i + 1) / 3
        stoogeSort(arr, i, j - t)  # stooge sort the initial 2/3 of the data
        stoogeSort(arr, i + t, j)  # stooge sort the final 2/3 of the data
        stoogeSort(arr, i, j - t)  # stooge sort the initial 2/3 of the data again

    return arr


# wrapper function to compute the initial value of j rather then
# detecting the sentinel value NONE
def stooge(arr): return stoogeSort(arr, 0, len(arr) - 1)


def main():
    data_size = input("How many elements do you want to insert?\t")
    data = getData(data_size)

    print "Before Sorting -> {0:}".format(data)

    print "After Sorting -> {0:}".format(stooge(data))


if __name__ == '__main__':
    main()
