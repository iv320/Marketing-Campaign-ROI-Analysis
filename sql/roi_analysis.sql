-- Campaign ROI Analysis
-- SQL equivalent of the python analysis

-- 1. Campaign Rankings with Classification
SELECT 
    campaign_name,
    channel,
    spend,
    revenue,
    roi,
    CASE 
        WHEN roi > 100 THEN 'Top Performer'
        WHEN roi > 0 THEN 'Average'
        ELSE 'Loss-Making'
    END as performance_category
FROM MetrifiedData -- assuming CTE from prep script avalable, or:
-- (Redefining minimal CTE for standalone execution context)
/*
WITH MetrifiedData AS (
    SELECT *, (revenue - spend)/spend * 100 as roi FROM marketing_campaigns
)
*/
ORDER BY roi DESC;

-- 2. Top 20 Campaigns
SELECT TOP 20
    campaign_name,
    roi,
    revenue
FROM marketing_campaigns_with_metrics
ORDER BY roi DESC;

-- 3. Channel ROI Aggregation
SELECT 
    channel,
    SUM(spend) as total_spend,
    SUM(revenue) as total_revenue,
    AVG(roi) as average_roi,
    COUNT(CASE WHEN roi > 0 THEN 1 END) as profitable_campaign_count
FROM marketing_campaigns_with_metrics
GROUP BY channel
ORDER BY average_roi DESC;
