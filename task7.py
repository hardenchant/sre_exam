import sys


def eratosthenes(n):
    """
    Get all primes from 1 to n. 0 if not prime, else number
    :param n:
    :return: [0, 2, 3, ..., n]
    """
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return [i for i in sieve[1:] if i != 0]


def is_exists_sublist_k_with_c_primes(primes_list, k, c):
    """
    Is exists sublist of len `k` with `c` primes
    :param primes_list:
    :param k:
    :param c:
    :return: -1 if not exists else first sublist number
    """
    if c > len(primes_list):
        return -1

    for start_point in range(len(primes_list) - c):
        sublist = primes_list[start_point: start_point + c]
        if sublist[-1] - sublist[0] <= k:
            return sublist[0]
    return -1


def main():
    kcs = []
    for _ in range(int(sys.stdin.readline().strip())):
        kcs.append(
            [int(i) for i in sys.stdin.readline().strip().split(' ')]
        )
    primes_list = eratosthenes(10 ** 5)
    for k, c in kcs:
        sys.stdout.write(str(is_exists_sublist_k_with_c_primes(primes_list, k, c)) + '\n')


if __name__ == "__main__":
    main()
