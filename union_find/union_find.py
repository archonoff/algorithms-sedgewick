from sys import stdin


class UnionFindBase:
    def __init__(self, n: int):
        self.n = n
        self.array = list(range(n))

    def connected(self, p: int, q: int) -> bool:
        raise NotImplementedError

    def union(self, p: int, q: int) -> None:
        raise NotImplementedError


class QuickFind(UnionFindBase):
    def connected(self, p: int, q: int) -> bool:
        """Find takes O(1) time"""
        return self.array[p] == self.array[q]

    def union(self, p: int, q: int) -> None:
        """Union takes O(n) time"""
        for i in range(len(self.array)):
            if self.array[i] == self.array[p]:
                self.array[i] = self.array[q]


class QuickUnion(UnionFindBase):
    """Union works fast because of lazy evaluation"""

    def root(self, i: int):
        """All algorithm complexity is here"""
        d = 0
        while i != self.array[i]:
            self.array[i] = self.array[self.array[i]]
            i = self.array[i]
            d += 1
        return i, d

    def union(self, p: int, q: int) -> None:
        i, i_d = self.root(p)
        j, j_d = self.root(q)
        if i_d > j_d:
            self.array[j] = i
        else:
            self.array[i] = j   # or self.array[j] - must be the same because for root element they should be equal

    def connected(self, p: int, q: int) -> bool:
        i, _ = self.root(p)
        j, _ = self.root(q)
        return i == j


def main():
    n = int(input())
    uf = QuickUnion(n)
    for line in stdin:
        p, q = [int(s) for s in line.split()]
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f'{p} {q}')


if __name__ == '__main__':
    main()
