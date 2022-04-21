import sys
from collections import deque

class Graph:
    def __init__(self, graph_type):
        self.graph_type = graph_type
        self.graph = self.read()

    def read(self):
        graph = dict()

        for line in sys.stdin:
            if not line.strip():
                continue

            v1, v2 = line.strip().split(' ')
            
            if v1 not in graph:
                graph[v1] = set()

            if v2 not in graph:
                graph[v2] = set()

            graph[v1].add(v2)

            if self.graph_type == 'u':
                graph[v2].add(v1)

        for v, row in graph.items():
            graph[v] = sorted(list(row))

        return graph

    def dfs(self, start):
        used = {v:False for v in self.graph}
        stack = []
        stack.append(start)

        while stack:
            vertex = stack.pop()

            if used[vertex]:
                continue
            
            used[vertex] = True
            print(vertex)

            for node in self.graph[vertex][::-1]:
                if not used[node]:
                    stack.append(node)

    def bfs(self, start):
        used = {v:False for v in self.graph} 
        q = deque()
        q.append(start)
        used[start] = True

        while q:
            u = q.popleft()
            print(u)

            for v in self.graph[u]:
                if not used[v]:
                    used[v] = True
                    q.append(v)


graph_type, start, search_type = input().split(' ')
graph = Graph(graph_type)

if search_type == "d":
    graph.dfs(start)
else:
    graph.bfs(start)
