# NJ_socialmedia

This repository contains code and data related to a social media analysis of Nanjing, China. Due to Weibo's Terms of Service prohibiting the sharing of users' posts, we provide aggregated statistical data, analysis scripts, and a sample of anonymized posts for reproducibility purposes.

## Repository Contents

1. **Analysis Scripts**:
   - `correlation.py`: Generates correlation maps
   - `njattentionheatmap.py`: Creates heatmaps showing post category percentages
   - `njattention.py`: Visualizes post counts for different areas
   - `njsentiment.py`: Produces sentiment statistics for different areas

2. **Data Files**:
   - `nanjing.json`: GeoJSON file containing geographical data for Nanjing districts
   - `keywords.txt`: List of keywords used for post collection
   - `nanjing_sentiment_data.csv`: Sentiment analysis data
   - `Post_NonSensitive.csv`: Sample of 450 anonymized posts

## Usage

To reproduce the analysis:

1. Clone this repository
2. Install required dependencies (list dependencies here)
3. Run the desired analysis script, e.g., `python correlation.py`

## Data Description

- The `nanjing.json` file contains geographical boundaries for Nanjing districts.
- `keywords.txt` lists the keywords used to collect relevant tweets.
- `nanjing_sentiment_data.csv` contains aggregated sentiment data for the analyzed posts.
- `Post_NonSensitive.csv` provides a sample of 450 anonymized posts for reference.


## Full Dataset Access

For academic purposes, the complete dataset of 76,288 image-text posts is available. To request access to this dataset, please contact Professor Lu Zhengyang at luzhengyang@jiangnan.edu.cn. 
Please note that this full dataset is intended for academic research only and should be used in compliance with all relevant ethical guidelines and data protection regulations.

## Ethical Considerations
We have taken care to comply with Weibo's Terms of Service by not sharing individual user posts publicly. The provided sample has been anonymized to protect user privacy. Researchers accessing the full dataset are expected to maintain the same level of privacy and ethical standards in their use of the data.

## Citation

If you use this data or code in your research, please cite.


