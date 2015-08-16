'''
Programming assignment 4

Kosaraju's SCC algorithm

Find the sizes of the 5 largest SCCs
'''
import sys
import threading


def build_graph(filename):
    g, g_rev = [], []
    with open(filename) as f:
        for line in f:
            u, v = map(int, line.split())
            m = max(u, v)
            while len(g) < m:
                g.append([])
            while len(g_rev) < m:
                g_rev.append([])
            g[u-1].append(v-1)
            g_rev[v-1].append(u-1)
    return g, g_rev


t = 0
vis = None
size = 0
f = None


def scc(g, g_rev):
    global t, vis, size, f

    n = len(g)
    t = 0
    vis = [False] * n
    f = [None] * n
    for i in reversed(xrange(n)):
        if not vis[i]:
            dfs1(g_rev, i)

    vis = [False] * n
    res = []
    for i in reversed(xrange(n)):
        if not vis[f[i]]:
            size = 0
            dfs2(g, f[i])
            res.append(size)
    return res


def dfs1(g_rev, u):
    global t, vis, f
    vis[u] = True
    for v in g_rev[u]:
        if not vis[v]:
            dfs1(g_rev, v)
    f[t] = u
    t += 1


def dfs2(g, u):
    global vis, size
    vis[u] = True
    for v in g[u]:
        if not vis[v]:
            dfs2(g, v)
    size += 1


def solve():
    g, g_rev = build_graph('SCC.txt')
    res = scc(g, g_rev)
    print ','.join(map(str, sorted(res, reverse=True)[:5]))


if __name__ == '__main__':
    sys.setrecursionlimit(2 ** 20)
    threading.stack_size(67108864)
    thread = threading.Thread(target=solve)
    thread.start()
