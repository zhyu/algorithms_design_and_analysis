'''
Programming assignment 5

Dijkstra's shortest-path algorithm

If there's no path, define the distance as 1000000
'''
import heapq


def build_graph(filename):
    g = []
    with open(filename) as f:
        for line in f:
            g.append([(v-1, w) for v, w in (map(int, edge.split(','))
                                            for edge in line.split()[1:])])
    return g


def dijkstra(g, s):
    h = []
    n = len(g)
    dist = [1000000] * n
    dist[s] = 0
    vis = [False] * n
    heapq.heappush(h, (0, s))
    while len(h):
        (_, u) = heapq.heappop(h)
        if vis[u]:
            continue
        vis[u] = True
        for v, w in g[u]:
            if not vis[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(h, (dist[v], v))
    return dist


g = build_graph('dijkstraData.txt')
dist = dijkstra(g, 0)
print ','.join((str(dist[x-1])
                for x in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]))
