def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for index in range(2, n):
        if n % index == 0:
            return False

    return   True
