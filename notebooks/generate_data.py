import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_marketing_data(num_campaigns=500):
    np.random.seed(42)  # For reproducibility
    random.seed(42)

    # Setup
    channels = ['Google Ads', 'Facebook', 'Instagram', 'Email', 'LinkedIn']
    segments = ['New', 'Returning', 'High-Value', 'Low-Value']
    
    data = []
    
    start_date = datetime(2025, 7, 1)
    
    for i in range(num_campaigns):
        campaign_id = f"CMP-{1000+i}"
        channel = random.choice(channels)
        segment = random.choice(segments)
        
        # Generate start date
        days_offset = random.randint(0, 180)
        c_start_date = start_date + timedelta(days=days_offset)
        
        # Channel specific modifiers (some channels are more expensive or have different conversion rates)
        if channel == 'Google Ads':
            cpc_base = 2.5
            ctr_base = 0.04
            conv_rate_base = 0.03
        elif channel == 'Facebook':
            cpc_base = 1.8
            ctr_base = 0.09
            conv_rate_base = 0.02
        elif channel == 'Instagram':
            cpc_base = 1.5
            ctr_base = 0.12 # Higher engagement
            conv_rate_base = 0.015
        elif channel == 'LinkedIn':
            cpc_base = 5.0
            ctr_base = 0.02
            conv_rate_base = 0.05 # Higher quality leads
        else: # Email
            cpc_base = 0.1 # Very low cost per "send" (approx)
            ctr_base = 0.15 # Open/Click rate
            conv_rate_base = 0.04

        # Generate Spend (Randomized per campaign size)
        # Small, Medium, Large campaigns
        camp_size = random.choice(['Small', 'Medium', 'Large'])
        if camp_size == 'Small':
            spend = np.random.uniform(500, 2000)
        elif camp_size == 'Medium':
            spend = np.random.uniform(2000, 10000)
        else:
            spend = np.random.uniform(10000, 50000)
            
        # Emails don't strictly have "Spend" in the same way, but let's model content/tool costs or just CPM
        if channel == 'Email':
            spend = spend * 0.1 # Cheaper
            
        # Calculate Impressions based on Spend and roughly CPM (Cost Per Mille)
        # High spend -> High impressions
        # Cost per impression varies by channel
        cpm = cpc_base * 10 # Rough approximation
        impressions = int((spend / (cpm/1000)) * np.random.uniform(0.8, 1.2))
        
        # Clicks based on Impressions and CTR
        ctr = ctr_base * np.random.uniform(0.8, 1.2)
        clicks = int(impressions * ctr)
        
        # Ensure clicks <= impressions
        clicks = min(clicks, impressions)
        if clicks == 0: clicks = 1 # Avoid div by zero later
        
        # Conversions based on Clicks and Conv Rate
        conv_rate = conv_rate_base * np.random.uniform(0.8, 1.2)
        conversions = int(clicks * conv_rate)
        
        # Ensure conversions <= clicks
        conversions = min(conversions, clicks)
        
        # Revenue
        # Revenue depends on conversions and "Average Order Value" (AOV)
        # Segments might have different AOV
        if segment == 'High-Value':
            aov = np.random.uniform(150, 300)
        elif segment == 'Low-Value':
            aov = np.random.uniform(20, 50)
        else:
            aov = np.random.uniform(50, 150)
            
        revenue = round(conversions * aov, 2)
        
        # Customer ID (Randomly assigned, some overlap implies returning customers)
        customer_id = random.randint(10001, 15000)
        
        campaign_name = f"{channel}_{camp_size}_{segment}_{c_start_date.strftime('%b')}"

        data.append({
            'campaign_id': campaign_id,
            'campaign_name': campaign_name,
            'channel': channel,
            'impressions': impressions,
            'clicks': clicks,
            'spend': round(spend, 2),
            'conversions': conversions,
            'revenue': revenue,
            'customer_id': customer_id,
            'customer_segment': segment,
            'campaign_start_date': c_start_date.strftime('%Y-%m-%d')
        })

    df = pd.DataFrame(data)
    
    # Save
    output_path = r'C:\Users\Isha\.gemini\antigravity\scratch\marketing-analytics-roi\data\marketing_campaigns.csv'
    df.to_csv(output_path, index=False)
    print(f"Dataset generated with {len(df)} records at {output_path}")
    
    # Display sample
    print(df.head())

if __name__ == "__main__":
    generate_marketing_data()
