# Trabalho 3 — Problema do Carteiro Chinês

**Disciplina:** Grafos  
**Professor:** Me. Ricardo Carubbi  
**Grupo:**
- Anselmo Teixeira — 2410414
- João Marcelo Jucá — 2410392
- Thigo Victor Ferreira — 2410413

---

## Problema

O Problema do Carteiro Chinês consiste em encontrar o percurso fechado de menor custo que percorre todas as arestas de um dígrafo ponderado ao menos uma vez. O percurso ótimo existe quando o grafo admite circuito euleriano, ou seja, quando todos os vértices têm grau de entrada igual ao grau de saída.

---

## Instância utilizada

O dígrafo original possui **6 vértices** e **11 arestas dirigidas ponderadas**.

Ao calcular os graus de cada vértice, identificamos os seguintes vértices desbalanceados:

| Vértice | Grau Entrada | Grau Saída | Delta |
|---------|-------------|------------|-------|
| v1 | 1 | 2 | +1 |
| v2 | 1 | 2 | +1 |
| v3 | 2 | 2 | 0 |
| v4 | 2 | 2 | 0 |
| v5 | 3 | 2 | −1 |
| v6 | 2 | 1 | −1 |

v1 e v2 têm mais saídas do que entradas; v5 e v6 têm mais entradas do que saídas. O grafo original **não admite** circuito euleriano.

---

## Eulerização manual

Para balancear o grafo, adicionamos arestas representando caminhos que serão percorridos duas vezes no circuito ótimo. A escolha dos caminhos foi feita manualmente, sem uso de Floyd-Warshall nem método húngaro.

**Caminhos adicionados:**

**Caminho A** — equilibra v5 (delta −1) com v2 (delta +1):

```
v5 → v1 → v2   (arestas: v5→v1 peso 12, v1→v2 peso 10)   custo = 22
```

**Caminho B** — equilibra v6 (delta −1) com v1 (delta +1):

```
v6 → v3 → v4 → v5 → v1   (arestas: v6→v3 peso 22, v3→v4 peso 20, v4→v5 peso 5, v5→v1 peso 12)   custo = 59
```

**Total adicionado:** 6 arestas, custo 81.  
Após a inserção, todos os 6 vértices ficaram balanceados e o grafo admite circuito euleriano.

O grafo eulerizado está em `dados/entrada_eulerizada.txt` com **17 arestas**.

---

## Execução

**Pré-requisito:** Python 3.7 ou superior (sem dependências externas).

Entre na pasta `src/` e execute `main.py`:

```bash
cd src
python main.py
```

O programa irá:
1. Ler `dados/entrada_eulerizada.txt`
2. Exibir os graus de entrada e saída de cada vértice
3. Verificar se o grafo está balanceado
4. Executar o método de Hierholzer
5. Imprimir o circuito euleriano encontrado
6. Informar o custo total do circuito

**Saída esperada:**

```
=======================================================
  Problema do Carteiro Chinês — Circuito Euleriano
=======================================================

Dígrafo ponderado: 6 vértices, 17 arestas

Graus de entrada e saída por vértice:
  Vértice      Grau Entrada   Grau Saída
  --------------------------------------
  v1                      3            3
  v2                      2            2
  v3                      3            3
  v4                      3            3
  v5                      4            4
  v6                      2            2

Verificação: grafo BALANCEADO — todos os vértices têm
             grau de entrada == grau de saída.

Executando método de Hierholzer...

Circuito euleriano encontrado:
  v1 -> v2 -> v5 -> v1 -> v3 -> v4 -> v5 -> v1 -> v2 -> v4 -> v6 -> v3 -> v5 -> v6 -> v3 -> v4 -> v5 -> v1

Custo total do circuito: 276
```

---

## Vídeo explicativo

> **Link do vídeo:** 

O vídeo apresenta:
- identificação do grupo e tema do trabalho
- o problema e a instância adotada
- identificação dos vértices desbalanceados
- justificativa da eulerização manual
- explicação da implementação do método de Hierholzer
- execução completa do programa com leitura comentada da saída

---

## Estrutura do projeto

```
trabalho3-unidade2/
├── README.md
├── dados/
│   ├── entrada_original.txt      # dígrafo original (6 vértices, 11 arestas)
│   └── entrada_eulerizada.txt    # dígrafo eulerizado (6 vértices, 17 arestas)
└── src/
    ├── main.py                   # ponto de entrada
    ├── directed_edge.py          # DirectedEdge (baseado no algs4-py)
    ├── edge_weighted_digraph.py  # EdgeWeightedDigraph (baseado no algs4-py)
    ├── directed_eulerian_cycle.py# método de Hierholzer
    └── bag.py                    # Bag com lista ligada (baseado no algs4-py)
```
