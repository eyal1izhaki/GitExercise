def sum_1_100():
    return sum(range(1, 101))


def is_prime(num):
    for i in range(2, int(num/2)+1):
        if num%i == 0:
            return False
    return True

def main():
    for i in [5,6,7,14,152,60693]:
        print(f"Is {i} prime?", is_prime(i))
if __name__ == "__main__":
    main()