def sum_1_100():
    return sum(range(1, 101))


def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


def is_prime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True


def main():
    for i in [5, 6, 7, 14, 152, 60693]:
        print(f"Is {i} prime?", is_prime(i))

    for i in range(5, 9):
        print(str(i) + "!:", factorial(i))


if __name__ == "__main__":
    main()
