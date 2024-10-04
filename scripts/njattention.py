# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:35:19 2024

@author: Administrator
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import json
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd

# Load Nanjing district boundaries
with open('nanjing.json', 'r', encoding='utf-8') as f:
    nanjing_data = json.load(f)

nanjing = gpd.GeoDataFrame.from_features(nanjing_data['features'])

# Load the real data
real_data = {
    'Xuanwu': 11439, 'Gulou': 13726, 'Jianye': 9151, 'Qinhuai': 10675,
    'Pukou': 6099, 'Qixia': 5337, 'Yuhuatai': 4572, 'Jiangning': 6861,
    'Luhe': 3810, 'Lishui': 3047, 'Gaochun': 1526
}

category_data = {
    'Built Environment': [2.561413, 18.803730, 22.227079, 16.000000, 18.773569, 13.790519, 13.626422, 7.768547, 20.551181, 16.409583, 13.564875],
    'Natural Environment': [20.070811, 14.659041, 15.059557, 13.277752, 22.118380, 20.648304, 18.592957, 18.145968, 28.582678, 33.967509, 19.987549],
    'Cultural Heritage': [28.561062, 15.999416, 13.559173, 25.180328, 10.049189, 19.336330, 23.599738, 13.585483, 14.094488, 17.033147, 16.841416],
    'Social Dynamics': [10.620684, 17.022294, 15.606546, 15.429977, 14.933758, 14.520815, 13.978346, 18.624110, 17.322835, 15.851986, 14.547837],
    'Economic Factors': [11.989685, 23.575405, 20.143154, 15.345199, 14.018036, 25.294922, 13.166010, 41.641161, 12.125984, 7.548081, 14.876146],
    'Urban Mobility': [10.259638, 9.678712, 10.704842, 10.050117, 14.082636, 7.138279, 11.810368, 8.221830, 8.527559, 8.565802, 9.436435],
    'Governance & Planning': [15.936708, 12.261402, 8.698503, 10.716628, 13.034924, 11.485853, 13.188976, 6.442210, 4.015748, 7.220217, 17.496723]
}

# Define categories
categories = list(category_data.keys())

# Create a custom colormap suitable for publication
colors = ['#FEEEEE', '#F22222', '#500000']  # Light gray to light salmon to tomato
n_bins = 100
cmap = LinearSegmentedColormap.from_list('custom', colors, N=n_bins)

# Set up the matplotlib style for scientific publication
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['axes.labelsize'] = 8
plt.rcParams['xtick.labelsize'] = 6
plt.rcParams['ytick.labelsize'] = 6
plt.rcParams['legend.fontsize'] = 6
plt.rcParams['figure.titlesize'] = 10

# Create a figure for each main category
for category in categories:
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Create a copy of the GeoDataFrame with attention data
    nanjing_attention = nanjing.copy()
    nanjing_attention['attention'] = category_data[category]
    
    # Normalize the data to [0, 1] range
    min_val = min(category_data[category])
    max_val = max(category_data[category])
    nanjing_attention['attention_normalized'] = (nanjing_attention['attention'] - min_val) / (max_val - min_val)
    
    # Plot the map
    nanjing_attention.plot(column='attention_normalized', ax=ax, 
                           cmap=cmap, edgecolor='#FFFFFF', linewidth=0.5)
    
    ax.set_title(category, fontsize=12, fontweight='bold')
    ax.axis('off')
    
    # Add a colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min_val, vmax=max_val))
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label('Attention (%)', rotation=270, labelpad=15)
    
    # Add labels for each district
    for idx, row in nanjing_attention.iterrows():
        ax.annotate(text=f"{row['attention']:.2f}%", 
                    xy=row['geometry'].centroid.coords[0], 
                    ha='center', va='center', fontsize=6)
    
    plt.tight_layout()
    plt.savefig(f'nanjing_{category.lower().replace(" ", "_")}_attention.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()

print("All attention maps have been generated as PNG files.")