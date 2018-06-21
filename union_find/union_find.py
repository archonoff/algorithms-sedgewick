from sys import stdin
import numpy as np


class UF:
    connections = None

    def __init__(self, n: int):
        self.n = n
        self.array = list(range(n))

    def connected(self, p: int, q: int) -> bool:
        return self.array[p] == self.array[q]

    def union_a(self, p: int, q: int) -> None:
        # 13 ms ± 358 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
        for i in range(len(self.array)):
            if self.array[i] == p:
                self.array[i] = q

    def union_b(self, p: int, q: int) -> None:
        # 7.83 ms ± 215 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
        for i, value in enumerate(self.array):
            if value == p:
                self.array[i] = q

    def union_b2(self, p: int, q: int) -> None:
        # 15.5 ms ± 202 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
        for i, _ in enumerate(self.array):
            if self.array[i] == p:
                self.array[i] = q

    def union_c(self, p: int, q: int) -> None:
        # было неверно
        # 11.4 ms ± 241 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
        # новое
        # 11.7 ms ± 1.01 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
        self.array = [q if value == p else i for i, value in enumerate(self.array)]

    def union_c2(self, p: int, q: int) -> None:
        # неверно
        # 7.39 ms ± 89.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
        self.array = [p if value == p else q for value in self.array]

class UF_np:
    connections = None

    def __init__(self, n: int):
        self.n = n
        self.array = np.arange(n)

    def connected(self, p: int, q: int) -> bool:
        return self.array[p] == self.array[q]

    def union_np_a(self, p: int, q: int) -> None:
        # 37 ms ± 671 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
        for i in range(self.array.shape[0]):
            if self.array[i] == p:
                self.array[i] = q

    def union_np_b(self, p: int, q: int) -> None:
        # 78.9 µs ± 1.99 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
        self.array[self.array == p] = q


uf = UF(100000)
uf_np = UF_np(100000)


def test_a():
    uf.union_a(2, 10)


def test_b():
    uf.union_b(3, 11)


def test_b2():
    uf.union_b2(4, 12)


def test_c():
    uf.union_c(5, 13)


def test_c2():
    uf.union_c2(6, 14)


def test_np_a():
    uf_np.union_np_a(7, 15)


def test_np_b():
    uf_np.union_np_b(8, 16)


def test_equality():
    uf_a = UF(10)
    uf_a.union_a(2, 9)

    uf_b = UF(10)
    uf_b.union_b(2, 9)

    uf_b2 = UF(10)
    uf_b2.union_b2(2, 9)

    uf_c = UF(10)
    uf_c.union_c(2, 9)

    uf_np = UF_np(10)
    uf_np.union_np(2, 9)

    print(uf_a.array)
    print(uf_b.array)
    print(uf_b2.array)
    print(uf_c.array)
    print(uf_np.array)




def main():
    n = int(input())
    uf = UF(n)
    print(uf.array)
    uf.union(1,1)
    print(uf.array)
    return
    for line in stdin:
        p, q = [int(s) for s in line.split()]
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f'{p} {q}')


if __name__ == '__main__':
    main()
