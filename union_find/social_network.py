from sys import stdin


'''
Social network connectivity. Given a social network containing nn members and a log file containing mm timestamps 
at which times pairs of members formed friendships, design an algorithm to determine the earliest time at which 
all members are connected (i.e., every member is a friend of a friend of a friend ... of a friend). Assume that 
the log file is sorted by timestamp and that friendship is an equivalence relation. The running time of your 
algorithm should be m * log(n) or better and use extra space proportional to n.
'''


class UnionFindSocial:
    def __init__(self, n):
        self.n = n
        self.array = list(range(n))
        self.sz = [1 for _ in range(self.n)]        # store a size of trees in root elements of corresponding trees

    def root(self, i: int):
        d = 0
        while i != self.array[i]:
            self.array[i] = self.array[self.array[i]]
            i = self.array[i]
            d += 1
        return i, d

    def all_connected(self, size):
        return size == self.n

    def union(self, p: int, q: int):
        # Friendship
        i, i_d = self.root(p)
        j, j_d = self.root(q)

        if i_d > j_d:
            self.array[j] = i
            self.sz[j] += self.sz[i]
            size = self.sz[j]
        else:
            self.array[i] = j
            self.sz[i] += self.sz[j]
            size = self.sz[i]

        # If size of new graph equals to N all users are connected
        if self.all_connected(self.sz[j]):
            return 'All users are connected'

    def connected(self, p: int, q: int) -> bool:
        i, _ = self.root(p)
        j, _ = self.root(q)
        return i == j


def main():
    n = int(input())
    uf = UnionFindSocial(n)
    for line in stdin:
        p, q = [int(s) for s in line.split()]
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f'{p} {q}')


if __name__ == '__main__':
    main()
