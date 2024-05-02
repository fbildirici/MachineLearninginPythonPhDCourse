import matplotlib.pyplot as plt
import networkx as nx

def draw_system_diagram():
    # Grafı oluştur
    G = nx.DiGraph()

    # Düğümleri ekle
    nodes = ["Geliştirici Aktiviteleri", "Performans Verileri Toplama", "Metrik Hesaplama",
             "Akıllı Sözleşme Tetikleme", "Token Hesaplama", "Token Dağıtımı"]
    G.add_nodes_from(nodes)

    # Bağlantıları ekle
    edges = [("Geliştirici Aktiviteleri", "Performans Verileri Toplama"),
             ("Performans Verileri Toplama", "Metrik Hesaplama"),
             ("Metrik Hesaplama", "Akıllı Sözleşme Tetikleme"),
             ("Akıllı Sözleşme Tetikleme", "Token Hesaplama"),
             ("Token Hesaplama", "Token Dağıtımı")]
    G.add_edges_from(edges)

    # Pozisyonları belirle (opsiyonel)
    pos = nx.spring_layout(G)

    # Düğümleri çiz
    nx.draw(G, pos, with_labels=True, node_size=7000, node_color='skyblue', font_size=9, font_weight='bold')

    # Bağlantıları çiz
    nx.draw_networkx_edges(G, pos, arrows=True)

    # Göster
    plt.title('Sistem Mimarisi ve Akış Şeması')
    plt.show()

draw_system_diagram()
