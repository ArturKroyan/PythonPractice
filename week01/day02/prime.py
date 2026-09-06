def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


for number in range(1, 201):
    if is_prime(number):
        print(number)