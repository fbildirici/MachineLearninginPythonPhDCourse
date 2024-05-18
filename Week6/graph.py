import matplotlib.pyplot as plt
import networkx as nx

# Grafiği oluştur
G = nx.DiGraph()

# Tokenomics yapısı düğümleri
nodes = [
    "Developer Contributions", "Smart Contracts", "Vesting", "Staking",
    "Token Allocation", "Token Distribution", "Economic Cycle", "Token Use",
    "Education", "Collaboration", "Product/Service Exchange"
]

# Düğümleri ekle
G.add_nodes_from(nodes)

# Bağlantıları ekle
edges = [
    ("Developer Contributions", "Smart Contracts"),
    ("Smart Contracts", "Vesting"),
    ("Smart Contracts", "Staking"),
    ("Vesting", "Token Allocation"),
    ("Staking", "Token Allocation"),
    ("Token Allocation", "Token Distribution"),
    ("Token Distribution", "Economic Cycle"),
    ("Economic Cycle", "Token Use"),
    ("Token Use", "Education"),
    ("Token Use", "Collaboration"),
    ("Token Use", "Product/Service Exchange")
]

G.add_edges_from(edges)

# Düğüm pozisyonlarını belirle
pos = {
    "Developer Contributions": (0, 3),
    "Smart Contracts": (1, 3),
    "Vesting": (2, 4),
    "Staking": (2, 2),
    "Token Allocation": (3, 3),
    "Token Distribution": (4, 3),
    "Economic Cycle": (5, 3),
    "Token Use": (6, 3),
    "Education": (7, 4),
    "Collaboration": (7, 3),
    "Product/Service Exchange": (7, 2)
}

# Grafiği çiz
plt.figure(figsize=(10, 6))
nx.draw_networkx(G, pos, node_size=1500, node_color='skyblue', font_size=10, font_weight='bold', arrowsize=15, edge_color='grey')
plt.title("Ideal Tokenomics Diagram")
plt.show()
