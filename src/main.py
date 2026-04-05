import os
import sys

from edge_weighted_digraph import EdgeWeightedDigraph
from directed_eulerian_cycle import DirectedEulerianCycle


def vertex_name(v):
    """Converte índice 0-based para notação (v1, v2, ...)."""
    return "v" + str(v + 1)


def load_graph(path):
    """Lê o dígrafo ponderado a partir do arquivo no formato esperado."""
    with open(path, 'r') as f:
        return EdgeWeightedDigraph(file=f)


def print_degrees(G):
    print("Graus de entrada e saída por vértice:")
    print(f"  {'Vértice':<10} {'Grau Entrada':>14} {'Grau Saída':>12}")
    print("  " + "-" * 38)
    for v in range(G.V):
        print(f"  {vertex_name(v):<10} {G.indegree(v):>14} {G.outdegree(v):>12}")


def check_balanced(G):
    """Retorna True se todos os vértices têm grau de entrada == grau de saída."""
    for v in range(G.V):
        if G.indegree(v) != G.outdegree(v):
            return False
    return True


def main():
    # Determina o caminho para os arquivos de dados relativamente a este script
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    eulerized_path = os.path.join(base_dir, "dados", "entrada_eulerizada.txt")

    print("=" * 55)
    print("  Problema do Carteiro Chinês — Circuito Euleriano")
    print("=" * 55)

    # Lê o dígrafo eulerizado
    G = load_graph(eulerized_path)
    print(f"Dígrafo ponderado: {G.V} vértices, {G.E} arestas\n")

    # Exibe graus
    print_degrees(G)
    print()

    # Verifica balanceamento
    balanced = check_balanced(G)
    if balanced:
        print("Verificação: grafo BALANCEADO — todos os vértices têm")
        print("             grau de entrada == grau de saída.\n")
    else:
        print("AVISO: grafo NÃO está balanceado. Não existe circuito euleriano.\n")
        sys.exit(1)

    # Executa o método de Hierholzer
    print("Executando método de Hierholzer...")
    ec = DirectedEulerianCycle(G)

    if not ec.has_eulerian_cycle():
        print("ERRO: não foi possível encontrar um circuito euleriano.")
        print("      Verifique se o grafo é fortemente conexo.")
        sys.exit(1)

    # Exibe o circuito euleriano
    circuit = ec.cycle()
    circuit_str = " -> ".join(vertex_name(v) for v in circuit)
    print(f"\nCircuito euleriano encontrado:\n  {circuit_str}\n")

    # Exibe o custo total
    total = ec.total_weight()
    if total == int(total):
        print(f"Custo total do circuito: {int(total)}")
    else:
        print(f"Custo total do circuito: {total}")


if __name__ == "__main__":
    main()
