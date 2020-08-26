import sys


def get_sum_various_permutation_lens(permutation_list: list) -> int:
    permutation_dict = dict(list(enumerate([None] + permutation_list))[1:])
    cycle_lens = set()
    while permutation_dict:
        value, next_value = permutation_dict.popitem()
        cycle = [value]
        while permutation_dict:
            if next_value in cycle:
                break
            cycle.append(next_value)
            next_value = permutation_dict.pop(next_value)
        cycle_lens.add(len(cycle))
    return sum(cycle_lens)


def main():
    sys.stdin.readline()
    permutation = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    get_sum_various_permutation_lens(permutation)
    sys.stdout.write(str(get_sum_various_permutation_lens(permutation)))


if __name__ == "__main__":
    main()
