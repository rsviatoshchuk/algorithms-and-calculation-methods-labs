def single_array_sum(array, n=None):
    if n is None or n > len(array):
        n = len(array)
    sum_of_array = 0
    for index in range(n):
        sum_of_array += array[index]
    return sum_of_array


def double_array_sum(array1, array2, n1=None, n2=None):
    if n1 is None or n1 > len(array1):
        n1 = len(array1)
    if n2 is None or n2 > len(array2):
        n2 = len(array2)

    sum_of_array = 0
    for i1 in range(n1):
        for i2 in range(n2):
            sum_of_array += array1[i1] + array2[i2]
    return sum_of_array


def single_array_product(array, n=None):
    if n is None or n > len(array):
        n = len(array)

    product = 0
    for index in range(n):
        product *= array[index]
    return product


def check_upper_bound(n):
    pass


def cyclic(a, b, n=None, p=None):
    return (single_array_product(a, n) + single_array_sum(b, n))/double_array_sum(a, b, n, p)


if __name__ == '__main__':
    print(cyclic([1, 2, 3], [3, 2, 1], 4, 4))
