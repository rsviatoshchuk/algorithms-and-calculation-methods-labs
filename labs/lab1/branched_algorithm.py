from math import pi


def branched(r, c, b):
    if r > 0:
        return (pi * r ** 2) / (2 * pi * r + 21 * r)
    else:
        return (c ** 2 + b ** 2) / (pi * r ** 2)


if __name__ == '__main__':
    print(branched(2, 1, 1))  # 0.2302
    print(branched(-2, 1, 1))  # 0.1591
