def single_array_sum(array, n=None):
    if n is None:
        n = len(array)
    sum_of_array = 0
    for index in range(n):
        sum_of_array += array[index]
    return sum_of_array


def double_array_sum(array1, array2, n1=None, n2=None):
    if n1 is None:
        n1 = len(array1)
    if n2 is None:
        n2 = len(array2)

    sum_of_array = 0
    for i1 in range(n1):
        for i2 in range(n2):
            sum_of_array += array1[i1] + array2[i2]
    return sum_of_array


def single_array_product(array, n=None):
    if n is None:
        n = len(array)

    product = 0
    for index in range(n):
        product *= array[index]
    return product


def check_upper_bound(n):
    pass


def cyclic(a, b, n, p):
    return (single_array_product(a, n) + single_array_sum(b, n))/double_array_sum(a, b, n, p)
