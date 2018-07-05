from sys import stdin


'''
Union-find with specific canonical element. Add a method find() to the union-find data type so that find(i)
returns the largest element in the connected component containing i. The operations, union(),
connected(), and find() should all take logarithmic time or better.

For example, if one of the connected components is {1,2,6,9}, then the find() method should return 9
 for each of the four elements in the connected components.
'''


class UnionFindCanonical:
    def __init__(self, n):
        self.n = n
        self.array = list(range(n))
        self.max_array = list(range(n))         # stores the biggest element in component with given root

    def root(self, i: int):
        d = 0
        while i != self.array[i]:
            self.array[i] = self.array[self.array[i]]
            i = self.array[i]
            d += 1
        return i, d

    def find(self, i):
        root, _ = self.root(i)
        return self.max_array[root]     # return the biggest element of component

    def union(self, p: int, q: int):
        i, i_d = self.root(p)
        j, j_d = self.root(q)

        if i_d > j_d:
            self.array[j] = i
            self.max_array[j] = max(self.max_array[i], self.max_array[j])
        else:
            self.array[i] = j
            self.max_array[j] = max(self.max_array[i], self.max_array[j])

    def connected(self, p: int, q: int) -> bool:
        i, _ = self.root(p)
        j, _ = self.root(q)
        return i == j


def main():
    n = int(input())
    uf = UnionFindCanonical(n)
    for line in stdin:
        p, q = [int(s) for s in line.split()]
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f'{p} {q}')
    print(uf.find(4))


if __name__ == '__main__':
    main()
