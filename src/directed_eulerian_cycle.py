class DirectedEulerianCycle:

    def __init__(self, G):
        self._cycle = None
        self._total_weight = 0.0

        # Verifica se o grafo tem arestas
        if G.E == 0:
            return

        # Constrói listas de adjacência consumíveis (cópia como listas indexáveis)
        adj = [list(G.adj[v]) for v in range(G.V)]
        adj_ptr = [0] * G.V

        # Escolhe o vértice inicial: o primeiro com arestas de saída
        start = -1
        for v in range(G.V):
            if len(adj[v]) > 0:
                start = v
                break

        if start == -1:
            return

        # Método de Hierholzer
        # Cada entrada da pilha é (vértice, aresta_de_chegada)
        # Para o vértice inicial a aresta de chegada é None
        stack = [(start, None)]
        circuit_vertices = []
        circuit_edges = []

        while stack:
            v, incoming_edge = stack[-1]
            if adj_ptr[v] < len(adj[v]):
                # Consome a próxima aresta de saída de v
                e = adj[v][adj_ptr[v]]
                adj_ptr[v] += 1
                stack.append((e.To(), e))
            else:
                # Nenhuma aresta de saída restante: adiciona ao circuito
                stack.pop()
                circuit_vertices.append(v)
                if incoming_edge is not None:
                    circuit_edges.append(incoming_edge)

        # O algoritmo produz o circuito em ordem inversa
        circuit_vertices.reverse()
        circuit_edges.reverse()

        # Verifica se todas as arestas foram consumidas (circuito euleriano válido)
        if len(circuit_vertices) == G.E + 1:
            self._cycle = circuit_vertices
            self._total_weight = sum(e.weight for e in circuit_edges)

    def has_eulerian_cycle(self):
        return self._cycle is not None

    def cycle(self):
        """Retorna a sequência de vértices do circuito euleriano."""
        return self._cycle

    def total_weight(self):
        """Retorna o custo total do circuito euleriano."""
        return self._total_weight
