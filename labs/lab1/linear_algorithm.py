from math import sin, cos, sqrt


def linear(a, b, x):
    return sin(a/b) + (sin(a/b))**2 + cos(x**2) + cos(sqrt(x))


if __name__ == '__main__':
    print(linear(3.14, 3.14, 1))  # 2.6301
