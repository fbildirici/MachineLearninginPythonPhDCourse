import pandas as pd
import matplotlib.pyplot as plt

# Veri setini oluşturma
data = {
    "Geliştirici ID": [1, 1, 2, 2],
    "Zaman Damgası": ["2024-01-01", "2024-02-01", "2024-01-01", "2024-02-01"],
    "Performans Puanı": [85, 90, 75, 80],
    "Alınan Token Miktarı": [100, 150, 80, 120]
}

df = pd.DataFrame(data)
df['Zaman Damgası'] = pd.to_datetime(df['Zaman Damgası'])

# Geliştiriciye göre verileri ayırma ve grafik çizme
for dev_id in df['Geliştirici ID'].unique():
    dev_data = df[df['Geliştirici ID'] == dev_id]
    plt.plot(dev_data['Zaman Damgası'], dev_data['Alınan Token Miktarı'], label=f'Geliştirici {dev_id}')

plt.xlabel('Zaman')
plt.ylabel('Alınan Token Miktarı')
plt.title('Zaman İçinde Geliştiricilere Dağıtılan Token Miktarları')
plt.legend()
plt.show()
