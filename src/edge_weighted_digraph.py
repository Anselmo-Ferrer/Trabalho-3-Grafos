from bag import Bag
from directed_edge import DirectedEdge


class EdgeWeightedDigraph:
    def __init__(self, v=0, **kwargs):
        self.V = v
        self.E = 0
        self.adj = [Bag() for _ in range(self.V)]
        self._indegree = [0] * self.V

        if 'file' in kwargs:
            in_file = kwargs['file']
            self.V = int(in_file.readline())
            self.adj = [Bag() for _ in range(self.V)]
            self._indegree = [0] * self.V
            num_edges = int(in_file.readline())
            for _ in range(num_edges):
                v, w, weight = in_file.readline().split()
                self.add_edge(DirectedEdge(int(v), int(w), float(weight)))

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        for i in range(self.V):
            adjs = " ".join(str(x) for x in self.adj[i])
            s += "%d: %s\n" % (i, adjs)
        return s

    def add_edge(self, e):
        self.adj[e.From()].add(e)
        self._indegree[e.To()] += 1
        self.E += 1

    def outdegree(self, v):
        return self.adj[v].size()

    def indegree(self, v):
        return self._indegree[v]

    def edges(self):
        result = []
        for v in range(self.V):
            for e in self.adj[v]:
                result.append(e)
        return result
