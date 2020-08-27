import sys


def floyd_uorshell(adj_matrix, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])
    return adj_matrix


def main():
    n, m = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    adj_matrix = [[10000 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        adj_matrix[i][i] = 0
    for _ in range(m):
        v1, v2 = [int(i) for i in sys.stdin.readline().strip().split(' ')]
        adj_matrix[v1 - 1][v2 - 1] = 1
        adj_matrix[v2 - 1][v1 - 1] = 1

    q = int(sys.stdin.readline().strip())
    queries = []
    for _ in range(q):
        v1, v2 = [int(i) - 1 for i in sys.stdin.readline().strip().split(' ')]
        queries.append((v1, v2))

    short_path_matrix = floyd_uorshell(adj_matrix, n)
    for v1, v2 in queries:
        short_path = short_path_matrix[v1][v2]
        if short_path >= 10000:
            sys.stdout.write(str(-1) + "\n")
        else:
            sys.stdout.write(str(short_path) + "\n")


if __name__ == "__main__":
    main()
