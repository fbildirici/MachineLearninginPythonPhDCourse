import matplotlib.pyplot as plt

categories = ['Stratejik', 'Stake Ödülleri', 'Sports Foundation', 'Private Sale', 'Liquidity', 'Team Share', 'Advertising', 'Project Development', 'Locked IEO', 'Unlocked IEO']
percentages = [21, 10, 5, 6.5, 15, 15, 5, 7.5, 5, 10]
colors = ['#B210B8', '#C532B9', '#D654BA', '#E776BB', '#F898BC', '#FFAABD', '#FFBCCE', '#FFCEDF', '#FFDFEF', '#FFF1FF']

plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Token Distribution', color='#B210B8')
plt.show()
