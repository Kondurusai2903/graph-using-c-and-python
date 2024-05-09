class disjointset:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.parent = [i for i in range(n+1)]

    def ultimateparent(self, node):
        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.ultimateparent(self.parent[node])
            return self.parent[node]
# ----------------------------------union by rank function ----------------------------------

    def unionbyrank(self, u, v):
        # find the the ultimate parents of u and v
        pu = self.ultimateparent(u)
        pv = self.ultimateparent(v)

        if pu == pv:
            return
        # the condition for connecting the ultimate parent by rank values
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
# -----------------------------------------------union by size---------------------------

    def unionbysize(self, u, v):
        # find the the ultimate parents of u and v
        pu = self.ultimateparent(u)
        pv = self.ultimateparent(v)
        if pu == pv:
            return
        # the condition for connecting the ultimate parent by size values
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
            self.rank[pv] += self.rank[pu]
        else:
            self.parent[pv] = pu
            self.rank[pu] += self.rank[pv]


sai = disjointset(7)
sai.unionbysize(1, 2)
sai.unionbysize(2, 3)
sai.unionbysize(4, 5)
sai.unionbysize(6, 7)
sai.unionbysize(5, 6)
if sai.ultimateparent(3) == sai.ultimateparent(7):
    print(True)
else:
    print(False)
sai.unionbysize(3, 7)
if sai.ultimateparent(3) == sai.ultimateparent(7):
    print(True)
else:
    print(False)

# if sai.ultimateparent(2) == sai.ultimateparent(3):
#     print(True)
# else:
#     print(False)
# print(sai.rank)
# print(sai.parent)
