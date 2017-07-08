import random


# initializes the list with random numbers
def getData(n):
    arr = [0] * n

    for i in range(n):
        arr[i] = random.randint(1, 100)

    return arr


# sorts the data based on the counting sort algorithm
def countingSort(arr, mx):
    count = [0] * (mx + 1)
    output = [0] * (len(arr))

    i = 0
    while i < len(arr):
        count[arr[i]] += 1
        i += 1

    i = 1
    while i < len(count):
        count[i] += count[i - 1]
        i += 1

    j = len(arr) - 1

    while j >= 0:
        output[count[arr[j] - 1]] = arr[j]
        count[arr[j]] -= 1
        j -= 1

    return output


def main():
    data_size = input("How many elements do you want to insert?\t")
    data = getData(data_size)
    print "Data before Sorting -> {0:}".format(data)

    print "Data after Sorting -> {0:}".format(countingSort(data, max(data)))


if __name__ == '__main__':
    main()
