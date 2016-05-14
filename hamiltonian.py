import networkx as nx

G = nx.Graph()

def getfor(formula):
    formula = formula[1:-1]
    clauses = formula.split("),(")
    tuplas = []
    for clause in clauses:
        clause = tuple(map(int,clause.split(",")))
        tuplas.append(clause)
    return tuplas

def main(str):
    g = getfor(str)
    G.add_edges_from(g)
    p = hamilton(G)
    return p

def hamilton(G):
    F = [(G,[G.nodes()[0]])]
    n = G.number_of_nodes()
    while F:
        graph,path = F.pop()
        confs = []
        for node in graph.neighbors(path[-1]):
            conf_p = path[:]
            conf_p.append(node)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g,conf_p))
        for g,p in confs:
            if len(p)==n:
                return p
            else:
                F.append((g,p))
    return None