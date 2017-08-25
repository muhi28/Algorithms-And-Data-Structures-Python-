import unittest
import random
import search_algorithms as sa


# initializes the list with random numbers
def getData(n):
    arr = [0] * n

    counter = 1

    for i in range(n):
        arr[i] = counter
        counter += 1

    return arr


# used generate a random number between 1 and 100
def getRandom(n):
    return random.randint(1, n)


class TestSearch(unittest.TestCase):
    """
        Test -> unsorted data (100 Elements)
    """

    def test_LinearUnsorted(self):
        print "Linear Search Algorithm Test Process STARTED ....\n"

        data = getData(100)
        print ("TEST 1 - Data -> {0:}\n".format(data))

        # search for random number between 1 and 100

        self.assertEqual(True, sa.linearSearch(data, getRandom(100)))

        # search for fixed number
        data = getData(100)
        print ("TEST 2 - Data -> {0:}\n".format(data))

        self.assertEqual(True, sa.linearSearch(data, 8))

        print "Linear Search Algorithm Test FINISHED ...\n"

    def test_BinaryUnsorted(self):
        print "Binary Search Algorithm Test STARTED ...\n"

        data = getData(100)

        print "Data -> {0:}\n".format(data)

        # search for random number between 1 and 100
        self.assertEqual(True, sa.binarySearch(data, getRandom(100)))

        # search for fixed number
        data = getData(100)
        print "Data -> {0:}\n".format(data)

        self.assertEqual(True, sa.binarySearch(data, getRandom(100)))

        print "Binary Search Algorithm Test FINISHED ...\n"

    def test_InterpolationUnsorted(self):
        print "Interpolation Search Algorithm Test STARTED ...\n"

        data = getData(100)
        print "Data -> {0:}\n".format(data)

        # search for random number between 1 and 100
        self.assertEqual(True, sa.interpolationSearch(data, getRandom(100)))

        # search for fixed number
        data = getData(100)
        print "Data -> {0:}\n".format(data)

        self.assertEqual(True, sa.interpolationSearch(data, getRandom(100)))

        print "Interpolation Search Algorithm FINISHED ...\n"

    """
        Tests -> sorted data (1000 Elements)
    """

    def test_LinearSorted(self):
        print "Linear Search Algorithm Test Process STARTED ....\n"

        data = getData(1000)
        print ("TEST 1 - Data -> {0:}\n".format(data))

        # search for random number between 1 and 100

        self.assertEqual(True, sa.linearSearch(data, getRandom(1000)))

        # search for fixed number
        data = getData(1000)
        print ("TEST 2 - Data -> {0:}\n".format(data))

        self.assertEqual(False, sa.linearSearch(data, 1500))

        print "Linear Search Algorithm Test FINISHED ...\n"

    def test_BinarySorted(self):
        print "Binary Search Algorithm Test STARTED ...\n"

        data = getData(1000)

        print "Data -> {0:}\n".format(data)

        # search for random number between 1 and 100
        self.assertEqual(True, sa.binarySearch(data, getRandom(1000)))

        # search for fixed number
        data = getData(1000)
        print "Data -> {0:}\n".format(data)

        self.assertEqual(True, sa.binarySearch(data, getRandom(1000)))

        print "Binary Search Algorithm Test FINISHED ...\n"

    def test_InterpolationSorted(self):
        print "Interpolation Search Algorithm Test STARTED ...\n"

        data = getData(1000)
        print "Data -> {0:}\n".format(data)

        # search for random number between 1 and 100
        self.assertEqual(True, sa.interpolationSearch(data, getRandom(1000)))

        # search for fixed number
        data = getData(1000)
        print "Data -> {0:}\n".format(data)

        self.assertEqual(True, sa.interpolationSearch(data, 178))

        print "Interpolation Search Algorithm FINISHED ...\n"


if __name__ == '__main__':
    unittest.main()
