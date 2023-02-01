from main import is_prime

MAX = 100
MIN = -MAX
PRIME_LIST = [
    2, 3, 5, 7,
    11, 13, 17, 19,
    23, 29,
    31, 37,
    41, 43, 47,
]


def test_is_prime():
    for index in range(MIN, 1 + MAX):

        is_exist_in_prime_list = list(filter(
            lambda x: x == index,
            PRIME_LIST,
        )).__len__() > 0

        assert is_exist_in_prime_list == is_prime(index)
