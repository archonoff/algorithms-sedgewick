from sys import stdin


class UF:
    def __init__(self, n: int):
        self.n = n
        self.array = list(range(n))

    def connected(self, p: int, q: int) -> bool:
        # quick find algorithm
        return self.array[p] == self.array[q]

    def union(self, p: int, q: int) -> None:
        for i in range(len(self.array)):
            if self.array[i] == self.array[p]:
                self.array[i] = self.array[q]


def main():
    n = int(input())
    uf = UF(n)
    for line in stdin:
        p, q = [int(s) for s in line.split()]
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f'{p} {q}')


if __name__ == '__main__':
    main()
