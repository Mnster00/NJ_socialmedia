import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import json
from matplotlib.colors import LinearSegmentedColormap

# Load Nanjing district boundaries
with open('nanjing.json', 'r', encoding='utf-8') as f:
    nanjing_data = json.load(f)

nanjing = gpd.GeoDataFrame.from_features(nanjing_data['features'])

# Read the CSV file
df = pd.read_csv('nanjing_sentiment_data.csv')

# Merge GeoDataFrame with sentiment data
nanjing = nanjing.merge(df, left_on='name', right_on='name')

# Create a custom colormap suitable for publication
colors = ['#FF0033', '#EEEEEE', '#07689F']  # Red to white to blue
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

# Define categories and their subcategories
categories = {
    'Built Environment': ['Urban Landscape', 'Architectural Landmarks', 'Urban Design', 'Residential Areas'],
    'Natural Environment': ['Green Spaces', 'Water Bodies', 'Environmental Quality', 'Climate Resilience'],
    'Cultural Heritage': ['Tangible Heritage', 'Intangible Heritage', 'Contemporary Culture', 'Culinary Heritage'],
    'Social Dynamics': ['Community Life', 'Social Cohesion', 'Safety', 'Education'],
    'Economic Factors': ['Commercial Activity', 'Employment', 'Innovation', 'Tourism'],
    'Urban Mobility': ['Public Transportation', 'Active Mobility', 'Traffic Management', 'Accessibility'],
    'Governance & Planning': ['Urban Policies', 'Civic Engagement', 'Smart City Initiatives', 'Sustainability Measures']
}

# Create a figure for each main category
for category, subcategories in categories.items():
    fig, axs = plt.subplots(1, len(subcategories), figsize=(16, 4))
    #fig.suptitle(f'Sentiment Analysis: {category}', fontsize=12, fontweight='bold')
    
    for idx, subcategory in enumerate(subcategories):
        column_name = f"{category} - {subcategory}"
        
        # Plot the map
        nanjing.plot(column=column_name, ax=axs[idx], 
                     cmap=cmap, vmin=-1, vmax=1, edgecolor='#FFFFFF', linewidth=0.5)
        
        axs[idx].set_title(subcategory, fontsize=12, fontweight='bold')
        axs[idx].axis('off')
    
    # Add a single colorbar for the entire figure
    cbar_ax = fig.add_axes([0.55, 0.09, 0.01, 0.7])
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=-1, vmax=1))
    sm.set_array([])
    cbar = fig.colorbar(sm, cax=cbar_ax)
    #cbar.set_label('Sentiment', fontsize=8)
    
    # Adjust the spacing between subplots
    plt.tight_layout(rect=[0, 0.03, 0.6, 0.95])
    
    # Further reduce the space between subplots
    plt.subplots_adjust(wspace=-0.5)
    
    plt.savefig(f'nanjing_{category.lower().replace(" ", "_")}_sentiment.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()

print("All sentiment maps have been generated as PNG files.")