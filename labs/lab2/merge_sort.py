import time


def merge_sort_with_time(array):
    start_time = time.time()
    return [merge_sort(array), time.time() - start_time]


def merge_sort(array):
    if len(array) < 2:
        return array
    middle = len(array)//2
    left = array[:middle]
    right = array[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    n = len(left) + len(right)
    array = [None]*n
    i1 = 0
    i2 = 0
    for i in range(n):
        if i1 == len(left):
            array[i] = right[i2]
            i2 += 1
        elif i2 == len(right):
            array[i] = left[i1]
            i1 += 1
        else:
            if left[i1] < right[i2]:
                array[i] = left[i1]
                i1 += 1
            else:
                array[i] = right[i2]
                i2 += 1
    return array


if __name__ == '__main__':
    # Test #1
    print("Test 1:")
    a = [44, 55, 12, 12, 94, 18, 6, 67, 7]
    sorted_a = [6, 7, 12, 12, 18, 44, 55, 67, 94]
    sorted_array = merge_sort(a)
    if sorted_a == sorted_array:
        print("OK")
    else:
        print("FAILED")

    # Test #2
    print("Test 2:")
    a = [44, 55, 12, 42, -94, 18, 6, 67]
    sorted_a = [-94, 6, 12, 18, 42, 44, 55, 67]
    sorted_array = merge_sort(a)
    if sorted_a == sorted_array:
        print("OK")
    else:
        print("FAILED")

    # Test #3
    print("Test 3:")
    a = [44, 55]
    sorted_a = [44, 55]
    sorted_array = merge_sort(a)
    if sorted_a == sorted_array:
        print("OK")
    else:
        print("FAILED")

    # Test #4
    print("Test 4:")
    a = [44]
    sorted_a = [44]
    sorted_array = merge_sort(a)
    if sorted_a == sorted_array:
        print("OK")
    else:
        print("FAILED")
