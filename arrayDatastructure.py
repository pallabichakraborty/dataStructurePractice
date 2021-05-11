def simpleArrayOperations(array):
    print("/*********************simpleArrayOperations*********************/")
    # O(N)
    print(array)
    # O(1)
    print(array[1])
    # O(N)
    print(array[:])
    # O(N)
    print(array[1:3])
    # O(N)
    print(array[:-1])
    # O(N)
    print(array[:-2])
    print("/******************************************/")

def linearSearch(array):
    print("/*********************linearSearch*********************/")
    # O(N)
    maximum = array[0]

    for num in array:
        if num > maximum:
            maximum = num

    print(maximum)
    print("/******************************************/")


def arrayManipulation():
    array = [10, 3, 4, 5]
    simpleArrayOperations(array)
    linearSearch(array)


if __name__ == "__main__":
    arrayManipulation()
    linearSearch()
