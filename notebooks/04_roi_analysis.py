import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def roi_analysis():
    input_path = r'C:\Users\Isha\.gemini\antigravity\scratch\marketing-analytics-roi\data\marketing_campaigns_cleaned.csv'
    output_dir = r'C:\Users\Isha\.gemini\antigravity\scratch\marketing-analytics-roi\visualizations'
    data_dir = r'C:\Users\Isha\.gemini\antigravity\scratch\marketing-analytics-roi\data'
    
    df = pd.read_csv(input_path)
    
    # 1. ROI Per Campaign & Classification
    # Already calculated in cleaning, but let's classify
    def classify_roi(roi):
        if roi > 1.0: return 'Top Performer' # > 100%
        elif roi > 0: return 'Average'
        else: return 'Loss-Making'
        
    df['Performance_Category'] = df['ROI'].apply(classify_roi)
    
    print("\nCampaign Performance Summary:")
    print(df['Performance_Category'].value_counts())
    
    # 2. Top Performing Campaigns
    top_campaigns = df.sort_values(by='ROI', ascending=False).head(20)
    print("\nTop 5 Campaigns by ROI:")
    print(top_campaigns[['campaign_name', 'channel', 'spend', 'revenue', 'ROI']])
    
    # Save rankings
    df[['campaign_id', 'campaign_name', 'channel', 'spend', 'revenue', 'ROI', 'Performance_Category']].to_csv(f"{data_dir}/campaign_roi_rankings.csv", index=False)
    
    # 3. Channel Impact on ROI
    channel_roi = df.groupby('channel')['ROI'].median().sort_values(ascending=False)
    print("\nMedian ROI by Channel:")
    print(channel_roi)
    
    # 4. Visualizations
    
    # Top 20 Campaigns ROI
    plt.figure(figsize=(12, 8))
    sns.barplot(x='ROI', y='campaign_name', data=top_campaigns, palette='magma')
    plt.title('Top 20 Campaigns by ROI')
    plt.xlabel('ROI')
    plt.axvline(x=1.0, color='r', linestyle='--', label='100% ROI')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/07_Top_20_Campaigns_ROI.png")
    plt.close()
    
    # ROI by Performance Category
    plt.figure(figsize=(8, 6))
    df['Performance_Category'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
    plt.title('Distribution of Campaign Performance Categories')
    plt.ylabel('')
    plt.savefig(f"{output_dir}/08_Performance_Category_Distribution.png")
    plt.close()
    
    print("ROI Analysis completed. Rankings saved to 'campaign_roi_rankings.csv'.")

if __name__ == "__main__":
    roi_analysis()
