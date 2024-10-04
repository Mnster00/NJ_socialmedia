# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:41:33 2024

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define districts and categories
districts = ['Xuanwu', 'Gulou', 'Jianye', 'Qinhuai', 'Pukou', 'Qixia', 'Yuhuatai', 'Jiangning', 'Luhe', 'Lishui', 'Gaochun']
categories = ['Built Environment', 'Natural Environment', 'Cultural Heritage', 'Social Dynamics', 'Economic Factors', 'Urban Mobility', 'Governance & Planning']

# Use the real data provided
category_percentages = pd.DataFrame({
    'Built Environment': [2.561413, 18.803730, 22.227079, 16.000000, 18.773569, 13.790519, 13.626422, 7.768547, 20.551181, 16.409583, 13.564875],
    'Natural Environment': [20.070811, 14.659041, 15.059557, 13.277752, 22.118380, 20.648304, 18.592957, 18.145968, 28.582678, 33.967509, 19.987549],
    'Cultural Heritage': [28.561062, 15.999416, 13.559173, 25.180328, 10.049189, 19.336330, 23.599738, 13.585483, 14.094488, 17.033147, 16.841416],
    'Social Dynamics': [10.620684, 17.022294, 15.606546, 15.429977, 14.933758, 14.520815, 13.978346, 18.624110, 17.322835, 15.851986, 14.547837],
    'Economic Factors': [11.989685, 23.575405, 20.143154, 15.345199, 14.018036, 25.294922, 13.166010, 41.641161, 12.125984, 7.548081, 14.876146],
    'Urban Mobility': [10.259638, 9.678712, 10.704842, 10.050117, 14.082636, 7.138279, 11.810368, 8.221830, 8.527559, 8.565802, 9.436435],
    'Governance & Planning': [15.936708, 12.261402, 8.698503, 10.716628, 13.034924, 11.485853, 13.188976, 6.442210, 4.015748, 7.220217, 17.496723]
}, index=districts)

# Total posts for each district
total_posts = pd.Series({
    'Xuanwu': 11439, 'Gulou': 13726, 'Jianye': 9151, 'Qinhuai': 10675,
    'Pukou': 6099, 'Qixia': 5337, 'Yuhuatai': 4572, 'Jiangning': 6861,
    'Luhe': 3810, 'Lishui': 3047, 'Gaochun': 1526
})

# Calculate the actual number of posts for each category
df = (category_percentages / 100 * total_posts.values.reshape(-1, 1)).round().astype(int)

# Set up the matplotlib figure
plt.figure(figsize=(12, 10))
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 0.5

# Create the heatmap
heatmap = sns.heatmap(df, annot=True, fmt='d', cmap='YlOrRd', 
            cbar_kws={'label': 'Number of Posts'},
            annot_kws={'size': 8}, linewidths=0.5, linecolor='white')

plt.title('Distribution of Posts Across Urban Dimensions in Nanjing Districts', fontsize=14, fontweight='bold')
plt.xlabel('Urban Dimensions', fontsize=12, fontweight='bold')
plt.ylabel('Districts', fontsize=12, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Increase colorbar label font size
cbar = heatmap.collections[0].colorbar
cbar.set_label('Number of Posts', fontsize=10, fontweight='bold')
cbar.ax.tick_params(labelsize=8)

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('nanjing_attention_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# Visualize category distribution
plt.figure(figsize=(12, 8))
category_percentages.plot(kind='bar', stacked=True, width=0.85)
plt.title('Category Distribution Across Nanjing Districts', fontsize=14, fontweight='bold')
plt.xlabel('Districts', fontsize=12, fontweight='bold')
plt.ylabel('Percentage', fontsize=12, fontweight='bold')
plt.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8, title_fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.ylim([0,100])
plt.tight_layout()
plt.savefig('category_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

print("Heatmap and category distribution plot have been generated.")

# Print the highest category for each district
print("\nHighest Category for Each District:")
for district in districts:
    highest_category = category_percentages.loc[district].idxmax()
    highest_value = category_percentages.loc[district].max()
    print(f"{district}: {highest_category} ({highest_value:.2f}%)")