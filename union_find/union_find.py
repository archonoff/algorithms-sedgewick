from sys import stdin


class UF:
    def __init__(self, N):
        self.N = N

    def connected(self, p, q) -> bool:
        return False     # todo

    def union(self, p, q) -> None:
        pass


def main():
    N = input()
    uf = UF(N)
    for line in stdin:
        p, q = line.split()
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f'{p} {q}')


if __name__ == '__main__':
    main()
