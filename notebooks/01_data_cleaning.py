import pandas as pd
import numpy as np

def clean_data():
    input_path = r'C:\Users\Isha\.gemini\antigravity\scratch\marketing-analytics-roi\data\marketing_campaigns.csv'
    output_path = r'C:\Users\Isha\.gemini\antigravity\scratch\marketing-analytics-roi\data\marketing_campaigns_cleaned.csv'
    
    print("Loading data...")
    df = pd.read_csv(input_path)
    print(f"Original shape: {df.shape}")
    
    # 1. Remove duplicates
    df = df.drop_duplicates()
    print(f"Shape after removing duplicates: {df.shape}")
    
    # 2. Handle missing values (Checking)
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("Missing values found, handling them...")
        # For simplicity in this synthetic data, we drop or fill. 
        # Since we generated it controlled, shouldn't be many, but good practice.
        df['impute_flag'] = False
        # Example: Fill missing spend with mean by channel (if any)
        # df['spend'] = df.groupby('channel')['spend'].transform(lambda x: x.fillna(x.mean()))
    else:
        print("No missing values found.")
        
    # 3. Ensure numeric types
    numeric_cols = ['impressions', 'clicks', 'spend', 'conversions', 'revenue']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
    # 4. Create Derived Metrics
    
    # CTR (Clicks / Impressions)
    # Avoid division by zero
    df['CTR'] = np.where(df['impressions'] > 0, df['clicks'] / df['impressions'], 0)
    
    # Conversion Rate (Conversions / Clicks)
    df['Conversion_Rate'] = np.where(df['clicks'] > 0, df['conversions'] / df['clicks'], 0)
    
    # ROI ((Revenue - Spend) / Spend)
    # Avoid division by zero
    df['ROI'] = np.where(df['spend'] > 0, (df['revenue'] - df['spend']) / df['spend'], 0)
    
    # Cost Per Conversion (Spend / Conversions)
    df['Cost_Per_Conversion'] = np.where(df['conversions'] > 0, df['spend'] / df['conversions'], np.nan)
    
    # 5. Date processing
    df['campaign_start_date'] = pd.to_datetime(df['campaign_start_date'])
    df['Month'] = df['campaign_start_date'].dt.strftime('%Y-%m')
    
    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
    print(df.head())
    
    # Summary stats
    print("\nSummary Statistics:")
    print(df[['spend', 'revenue', 'ROI']].describe())

if __name__ == "__main__":
    clean_data()
