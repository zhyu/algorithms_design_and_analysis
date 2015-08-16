'''
Programming assignment 3

Compute the Minimum Cuts of the given graph
'''


def build_graph(filename):
    with open(filename) as f:
        n = 200
        g = [[0] * n for _ in xrange(n)]
        for line in f:
            arr = map(int, line.split())
            for v in arr[1:]:
                g[arr[0]-1][v-1] = 1
        return g


def mincut(g):
    m = n = len(g)
    res = float('inf')
    v = range(n)
    while n > 1:
        vis = [False] * m
        u = v[0]
        vis[u] = True
        w = [g[u][v[i]] for i in xrange(n)]
        for i in xrange(1, n):
            t = -1
            for j in xrange(1, n):
                if not vis[v[j]] and (t < 0 or w[j] > w[t]):
                    t = j
            vis[v[t]] = True
            if i == n-1:
                res = min(res, w[t])
                for j in xrange(n):
                    g[v[j]][u] += g[v[t]][v[j]]
                    g[u][v[j]] += g[v[t]][v[j]]
                n -= 1
                v[t] = v[n]
            u = v[t]
            for j in xrange(1, n):
                if not vis[v[j]]:
                    w[j] += g[v[t]][v[j]]
    return res


g = build_graph('kargerMinCut.txt')
print mincut(g)
