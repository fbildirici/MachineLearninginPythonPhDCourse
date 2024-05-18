import matplotlib.pyplot as plt
import networkx as nx

# Grafiği oluştur
G = nx.DiGraph()

# Düğümleri tanımla
nodes = [
    "Developer", "Submit Performance Data", "Calculate Performance Score",
    "Token Allocation", "Token Distribution", "Get Tokens"
]

# Düğümleri ekle
G.add_nodes_from(nodes)

# Kenarları tanımla
edges = [
    ("Developer", "Submit Performance Data"),
    ("Submit Performance Data", "Calculate Performance Score"),
    ("Calculate Performance Score", "Token Allocation"),
    ("Token Allocation", "Token Distribution"),
    ("Token Distribution", "Get Tokens")
]

G.add_edges_from(edges)

# Düğüm pozisyonları
pos = {
    "Developer": (0, 4),
    "Submit Performance Data": (1, 3),
    "Calculate Performance Score": (2, 2),
    "Token Allocation": (3, 2),
    "Token Distribution": (4, 1),
    "Get Tokens": (5, 0)
}

# Grafiği çiz
plt.figure(figsize=(12, 8))
nx.draw_networkx(G, pos, node_size=2500, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20, edge_color='blue')
plt.title("Smart Contract Workflow Diagram")
plt.show()
