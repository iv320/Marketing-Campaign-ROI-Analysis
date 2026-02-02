import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

def customer_segmentation():
    input_path = r'C:\Users\Isha\.gemini\antigravity\scratch\marketing-analytics-roi\data\marketing_campaigns_cleaned.csv'
    output_dir = r'C:\Users\Isha\.gemini\antigravity\scratch\marketing-analytics-roi\visualizations'
    
    df = pd.read_csv(input_path)
    
    # 1. Pivot Table: Metrics by Segment
    segment_metrics = df.groupby('customer_segment').agg({
        'campaign_id': 'count',
        'spend': 'sum',
        'revenue': 'sum',
        'impressions': 'sum',
        'clicks': 'sum',
        'conversions': 'sum'
    }).reset_index()
    
    # Calculate derived metrics for segments
    segment_metrics['ROI'] = (segment_metrics['revenue'] - segment_metrics['spend']) / segment_metrics['spend'] * 100
    segment_metrics['CTR'] = (segment_metrics['clicks'] / segment_metrics['impressions']) * 100
    segment_metrics['Conversion_Rate'] = (segment_metrics['conversions'] / segment_metrics['clicks']) * 100
    
    print("\nCustomer Segment Metrics:")
    print(segment_metrics[['customer_segment', 'ROI', 'CTR', 'Conversion_Rate', 'revenue']])
    
    # 2. Visualization: Segment Performance Heatmap
    plt.figure(figsize=(10, 6))
    # Normalize for heatmap
    heatmap_data = segment_metrics.set_index('customer_segment')[['ROI', 'CTR', 'Conversion_Rate']]
    sns.heatmap(heatmap_data, annot=True, cmap='RdYlGn', fmt=".1f")
    plt.title('Customer Segment Performance Heatmap')
    plt.savefig(f"{output_dir}/05_Segment_Performance_Heatmap.png")
    plt.close()
    
    # 3. K-Means Clustering (Bonus)
    print("\nRunning K-Means Clustering on Campaign Performance...")
    # We'll cluster campaigns based on Spend and Conversion Rate to find "types" of campaigns/response patterns
    # Or we could cluster "Customers" if we had customer-level aggregation, but dataset is campaign-level 
    # where customer_id is linked. Let's cluster the *campaigns* by performance profile.
    
    features = df[['spend', 'Conversion_Rate']].copy()
    features = features.fillna(0)
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(scaled_features)
    
    # Minimize visual noise
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='spend', y='Conversion_Rate', hue='Cluster', data=df, palette='deep')
    plt.title('K-Means Clustering: Spend vs Conversion Rate')
    plt.xlabel('Spend')
    plt.ylabel('Conversion Rate')
    plt.savefig(f"{output_dir}/06_KMeans_Clustering.png")
    plt.close()
    
    print("Segmentation analysis and K-Means clustering completed.")

if __name__ == "__main__":
    customer_segmentation()
