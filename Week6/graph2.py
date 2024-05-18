import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Diyagram için temel ayarlar
fig, ax = plt.subplots(figsize=(12, 8))

# Renk paleti
box_color = 'skyblue'
arrow_color = 'grey'

# Modüller
modules = {
    "Developer Contributions": (0, 6),
    "Smart Contracts": (3, 6),
    "Vesting": (6, 7),
    "Staking": (6, 5),
    "Token Allocation": (9, 6),
    "Token Distribution": (12, 6),
    "Economic Cycle": (15, 6),
    "Token Use": (18, 6),
    "Education": (21, 7),
    "Collaboration": (21, 6),
    "Product/Service Exchange": (21, 5)
}

# Modül kutuları çiz
for name, pos in modules.items():
    ax.add_patch(mpatches.FancyBboxPatch((pos[0], pos[1]), 2, 1, boxstyle="round,pad=0.3", linewidth=1, edgecolor='black', facecolor=box_color))
    ax.text(pos[0] + 1, pos[1] + 0.5, name, ha='center', va='center', fontsize=12, fontweight='bold')

# Bağlantı okları çiz
connections = [
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

for start, end in connections:
    start_pos = modules[start]
    end_pos = modules[end]
    ax.arrow(start_pos[0] + 2, start_pos[1] + 0.5, end_pos[0] - start_pos[0] - 2, end_pos[1] - start_pos[1], head_width=0.3, head_length=0.3, fc=arrow_color, ec=arrow_color)

# Genel ayarlar
plt.xlim(-1, 24)
plt.ylim(4, 8.5)
plt.axis('off')
plt.title("Comprehensive Tokenomics Diagram", fontsize=15, fontweight='bold')
plt.show()
