def InitializeSingleSource(V, src):
    dist = [float("inf")] * V
    dist[src] = 0
    return dist


def Relax(u, v, w, dist):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        return True
    return False


def BellmanFord(edges, V, E, src):
    dist = InitializeSingleSource(V, src)
    for _ in range(V - 1):
        for u, v, w in edges:
            Relax(u, v, w, dist)
    for u, v, w in edges:
        if Relax(u, v, w, dist):
            return "Negative Cycle!"
    return dist


if __name__ == "__main__":
    V = int(input())
    E = int(input())
    edges = [list(map(int, input().split())) for _ in range(E)]
    result = BellmanFord(edges, V, E, 0)
    if result == "Negative Cycle!":
        print(result)
    else:
        print(" ".join(f"{num:.1f}" for num in result))

# Sample Input1
# 3
# 3
# 0 1 1
# 1 2 2
# 2 0 3

# Sample Output1
# 0.0 1.0 3.0


# Sample Input2
# 4
# 5
# 0 1 2
# 1 2 -4
# 2 0 -1
# 2 3 3
# 3 1 1

# Sample Output2
# Negative Cycle!


# Sample Input3
# 5
# 10
# 0 1 6
# 0 3 7
# 1 2 5
# 1 3 8
# 1 4 -4
# 2 1 -2
# 3 2 -3
# 3 4 9
# 4 2 7
# 4 0 2

# Sample Output3
# 0.0 2.0 4.0 7.0 -2.0
