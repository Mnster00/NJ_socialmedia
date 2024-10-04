# NJ_socialmedia

This repository contains code and data related to a social media analysis of Nanjing, China. Due to Weibo's Terms of Service prohibiting the sharing of users' posts, we provide aggregated statistical data, analysis scripts, and a sample of anonymized posts for reproducibility purposes.

## Repository Contents

1. **Analysis Scripts**:
   - `correlation.py`: Generates correlation maps
   - `njattentionheatmap.py`: Creates heatmaps showing tweet category percentages
   - `njattention.py`: Visualizes tweet counts for different areas
   - `njsentiment.py`: Produces sentiment statistics for different areas

2. **Data Files**:
   - `nanjing.json`: GeoJSON file containing geographical data for Nanjing districts
   - `keywords.txt`: List of keywords used for tweet collection
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
- `nanjing_sentiment_data.csv` contains aggregated sentiment data for the analyzed tweets.
- `Post_NonSensitive.csv` provides a sample of 450 anonymized posts for reference.

## Ethical Considerations

We have taken care to comply with Weibo's Terms of Service by not sharing individual user posts. The provided sample has been anonymized to protect user privacy.

## Citation

If you use this data or code in your research, please cite: (Add citation information here)

## Contact

For questions or further information, please contact: (Add contact information here)