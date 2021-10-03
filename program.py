def sum_1_100():
    return sum(range(1, 101))


def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


def main():
    for i in range(5, 9):
        print(str(i) + "!:", factorial(i))


if __name__ == "__main__":
    main()
