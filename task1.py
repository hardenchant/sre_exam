import sys


class CollacHypothesis:
    def __init__(self):
        # кэшируем результаты
        self.cache = dict()

    def get_p(self, num):
        cached = self.cache.get(num, None)
        if cached is not None:
            return cached
        if num == 1:
            return 0
        if num % 2:
            # нечет
            next_num = 3 * num + 1
        else:
            # чет
            next_num = num / 2
        p = self.get_p(next_num) + 1
        self.cache[num] = p
        return p

    def get_interval_sum(self, l, r):
        return sum([self.get_p(i) for i in list(reversed(range(l, r + 1)))])


def main():
    l, r = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    ch = CollacHypothesis()
    sys.stdout.write(str(ch.get_interval_sum(l, r)))


if __name__ == "__main__":
    main()
