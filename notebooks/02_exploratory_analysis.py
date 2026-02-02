import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_eda():
    input_path = r'C:\Users\Isha\.gemini\antigravity\scratch\marketing-analytics-roi\data\marketing_campaigns_cleaned.csv'
    output_dir = r'C:\Users\Isha\.gemini\antigravity\scratch\marketing-analytics-roi\visualizations'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    df = pd.read_csv(input_path)
    
    # Setup aesthetic
    sns.set(style="whitegrid")
    
    # 1. Distribution of ROI
    plt.figure(figsize=(10, 6))
    sns.histplot(df['ROI'], bins=30, kde=True, color='purple')
    plt.title('Distribution of Campaign ROI')
    plt.xlabel('ROI')
    plt.ylabel('Frequency')
    plt.savefig(f"{output_dir}/01_ROI_Distribution.png")
    plt.close()
    
    # 2. Channel Performance (Average ROI)
    plt.figure(figsize=(10, 6))
    avg_roi_channel = df.groupby('channel')['ROI'].mean().sort_values(ascending=False).reset_index()
    sns.barplot(x='channel', y='ROI', data=avg_roi_channel, palette='viridis')
    plt.title('Average ROI by Channel')
    plt.ylabel('Average ROI')
    plt.savefig(f"{output_dir}/02_Avg_ROI_by_Channel.png")
    plt.close()
    
    # 3. Spend vs Revenue
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='spend', y='revenue', hue='channel', data=df, alpha=0.7)
    plt.title('Spend vs Revenue by Channel')
    plt.xlabel('Spend ($)')
    plt.ylabel('Revenue ($)')
    # Add diagonal line for break-even
    max_val = max(df['spend'].max(), df['revenue'].max())
    plt.plot([0, max_val], [0, max_val], '--', color='red', label='Break-even')
    plt.legend()
    plt.savefig(f"{output_dir}/03_Spend_vs_Revenue.png")
    plt.close()
    
    # 4. Correlation Heatmap
    plt.figure(figsize=(10, 8))
    corr = df[['spend', 'revenue', 'impressions', 'clicks', 'conversions', 'ROI', 'CTR', 'Conversion_Rate']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix of Key Metrics')
    plt.savefig(f"{output_dir}/04_Correlation_Matrix.png")
    plt.close()

    print("EDA Visualizations generated in 'visualizations' folder.")

if __name__ == "__main__":
    run_eda()
