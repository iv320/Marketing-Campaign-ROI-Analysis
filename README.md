# Marketing Analytics - Campaign ROI Project

## 🎯 Project Objective
Build an end-to-end data analytics project to analyze marketing campaign performance, calculate ROI, and identify key drivers of profitability. This project demonstrates skills in **Python (Pandas, Matplotlib)**, **SQL**, and **Power BI**.

## 📂 Project Structure
```
marketing-analytics-roi/
├── data/
│   ├── marketing_campaigns.csv        # Raw synthetic dataset
│   └── marketing_campaigns_cleaned.csv # Processed dataset
├── notebooks/
│   ├── 00_data_generation.py          # Data generator
│   ├── 01_data_cleaning.py            # Data cleaning & metric calculation
│   ├── 02_exploratory_analysis.py     # EDA & Visualizations
│   ├── 03_customer_segmentation.py    # Segmentation & Clustering
│   └── 04_roi_analysis.py             # ROI ranking & analysis
├── sql/
│   ├── data_preparation.sql           # SQL queries for cleaning
│   └── roi_analysis.sql               # SQL queries for ROI
├── visualizations/                    # Output charts (png)
├── dashboard/
│   └── Marketing_Campaign_ROI_Dashboard.pbix # Power BI Dashboard
├── business_insights.md               # Final Business Report
└── requirements.txt                   # Python dependencies
```

## 🛠️ Technologies Used
- **Python**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **SQL**: CTEs, Aggregations, Window Functions
- **Power BI**: DAX Measures, Interactive Dashboarding

## 🚀 How to Run

### 1. Setup Environment
```bash
pip install -r requirements.txt
```

### 2. Run Analysis Scripts
Run the notebooks in order to generate data, clean it, and produce insights:
```bash
python notebooks/00_data_generation.py
python notebooks/01_data_cleaning.py
python notebooks/02_exploratory_analysis.py
python notebooks/03_customer_segmentation.py
python notebooks/04_roi_analysis.py
```

### 3. View Results
- Check the `visualizations/` folder for generated charts.
- Open `business_insights.md` for the strategic report.
- Open `dashboard/Marketing_Campaign_ROI_Dashboard.pbix` to interact with the Power BI Dashboard.

## 📊 Key Insights
- **Email** remains the most efficient channel (Highest ROI).
- **Campaign ROI** varies significantly by **Customer Segment**.
- **Recommendation**: Shift budget from low-performing Google Ads campaigns to high-converting LinkedIn campaigns for high-value segments.
