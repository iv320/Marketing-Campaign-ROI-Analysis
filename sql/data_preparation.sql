-- Marketing Analytics Data Preparation & Analysis
-- This script demonstrates how to clean and prepare data using SQL

-- 1. Create a CTE for Initial Cleaning (Removing duplicates would typically happen here if ID is not unique)
WITH CleanedData AS (
    SELECT DISTINCT
        campaign_id,
        campaign_name,
        channel,
        impressions,
        clicks,
        spend,
        conversions,
        revenue,
        customer_id,
        customer_segment,
        campaign_start_date
    FROM marketing_campaigns
    WHERE campaign_id IS NOT NULL 
),

-- 2. Calculate Derived Metrics
MetrifiedData AS (
    SELECT 
        *,
        -- CTR (Click Through Rate) %
        CASE WHEN impressions > 0 THEN (CAST(clicks AS FLOAT) / impressions) * 100 ELSE 0 END AS ctr,
        
        -- Conversion Rate %
        CASE WHEN clicks > 0 THEN (CAST(conversions AS FLOAT) / clicks) * 100 ELSE 0 END AS conversion_rate,
        
        -- ROI (Return on Investment) %
        CASE WHEN spend > 0 THEN ((revenue - spend) / spend) * 100 ELSE 0 END AS roi,
        
        -- Cost Per Conversion
        CASE WHEN conversions > 0 THEN spend / conversions ELSE NULL END AS cost_per_conversion
    FROM CleanedData
)

-- 3. Final Selection or Aggregation
-- Example: Channel Performance Summary
SELECT 
    channel,
    COUNT(campaign_id) as total_campaigns,
    SUM(spend) as total_spend,
    SUM(revenue) as total_revenue,
    AVG(roi) as avg_roi,
    AVG(ctr) as avg_ctr,
    AVG(conversion_rate) as avg_conversion_rate
FROM MetrifiedData
GROUP BY channel
ORDER BY total_revenue DESC;
