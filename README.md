# chocolate-sales-data-analysis
## Project Overview

This project demonstrates an end-to-end data analytics workflow applied to a chocolate sales dataset.
The analysis focuses on understanding sales performance across countries, products, time periods, and salespersons using multiple industry-standard tools.

The project showcases practical skills in data cleaning, analysis, visualization, and insight generation using Python, SQL, Excel, and Power BI.

##Project Objectives

Clean and prepare raw sales data for analysis

Identify top-performing countries, products, and salespersons

Analyze shipment trends and time-based sales patterns

Validate insights using SQL queries and Excel pivot tables

Build interactive dashboards for business decision-making

##Dataset Description

Records: 1000+ rows

Attributes:

Sales Person

Country

Product

Date

Amount

Boxes Shipped

Dataset versions used:

Raw Excel Dataset (original data)

Cleaned Dataset (validated and formatted)

Final CSV Dataset (used for SQL and Power BI)

##Data Cleaning & Preparation

Data cleaning was primarily performed using Python (Pandas):

Removed duplicate records

Converted Amount from currency format to numeric values

Standardized column names

Checked for missing values

Ensured consistent data types

Due to inconsistent date formats in the raw dataset, the Date column was further validated and formatted in Excel to ensure accurate monthly and trend-based analysis.
The final cleaned dataset was exported as a CSV file for cross-tool compatibility.

##Python Analysis (Pandas & Matplotlib)

Python was used for exploratory data analysis and visualization.

Key Analyses Performed:

Total sales per country

Top 10 products by boxes shipped

Top 5 salespersons by total sales amount

Outputs:

Bar charts generated using Matplotlib

Screenshots captured as analytical evidence

##SQL Analysis (MySQL)

SQL was used to perform structured queries and validate insights derived from Python analysis.

Key SQL Queries:

Country-wise total sales

Top 10 products by shipment volume

Count of sales records

Average sales amount per country

Highest selling product in the USA

Query scripts and output screenshots are included in the portfolio.

##Excel Analysis (Pivot Tables)

Excel was used for business-style analysis and verification through pivot tables.

Pivot Tables Created:

Total sales by country

Top salespersons by revenue

Monthly sales trend

Top 10 products by boxes shipped

Both raw and cleaned Excel files are included, along with pivot table screenshots.

##Power BI Dashboard

An interactive Power BI dashboard was developed to present insights visually.

Dashboard Features:

KPI Cards

Total Sales Amount

Total Boxes Shipped

Top Performing Country

Top Shipped Product

Sales performance visuals by country and product

Interactive filters for dynamic analysis

Dashboard screenshots are included as part of the portfolio.

##Key Business Insights

Australia and the United Kingdom emerged as the top-performing countries in terms of total sales revenue.

Sales analysis revealed that January recorded higher sales, while August showed comparatively lower sales, indicating seasonal variation.

50% Dark Bites was identified as the top shipped product overall, based on total boxes shipped.

In the USA market, Fruit & Nut Bars recorded the highest sales among all products.

A small group of top salespersons contributed a significant share of total revenue, highlighting strong individual performance impact.

Product demand varied across countries, suggesting region-specific customer preferences.

Shipment volume trends closely aligned with overall revenue patterns, indicating efficient distribution performance.

##Tools & Technologies Used

Python (Pandas, Matplotlib)

SQL (MySQL)

Microsoft Excel (Pivot Tables)

Power BI (Dashboards & KPIs)

##Project Structure
Chocolate_Sales_Portfolio/

 data/
    raw_chocolate_sales.xlsx 
    chocolate_sales_cleaned.xlsx
  

 python/
   data_cleaning.py
   charts_screenshots/
 
  sql/
   sql_output_screenshots_with_quaries/

 excel/
    pivot_tables_screenshots/

 power_bi/
   dashboard_screenshots/

 README.md

 Conclusion

This project demonstrates a complete data analytics lifecycle, combining data cleaning, analysis, validation, and visualization across multiple tools.
It reflects real-world analytical thinking and practical problem-solving skills suitable for a Junior Data Analyst / Data Analyst role.

https://github.com/fathimakhadheeja2004-dev/chocolate-sales-data-analysis/blob/main/README.md
