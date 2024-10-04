import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from njstat.csv
data = pd.read_csv('njstat.csv')

# Correlation heatmap
plt.figure(figsize=(20, 16))
corr_matrix = data.corr()
heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, fmt='.2f', annot_kws={'size': 10})

# Increase font size for xticks and yticks
plt.xticks(fontsize=12, rotation=90)
plt.yticks(fontsize=12)

# Increase font size for colorbar
cbar = heatmap.collections[0].colorbar
cbar.ax.tick_params(labelsize=12)

plt.title('Correlation Heatmap of New Jersey Statistics', fontsize=16)
plt.tight_layout()
plt.savefig('nj_correlation_heatmap.png', format='png', dpi=300, bbox_inches='tight')
plt.show()