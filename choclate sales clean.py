import pandas as pd

dataset=pd.read_csv(r"F:\raw chocolate sales.csv")

print(dataset)

import pandas as pd

# Load dataset (use raw string for Windows path)
dataset = pd.read_csv(r"F:\raw chocolate sales.csv")

# Clean column names (remove spaces)
dataset.columns = dataset.columns.str.strip().str.replace(' ', '_')

# Convert Date column to datetime
dataset['Date'] = pd.to_datetime(dataset['Date'], format='%Y-%m-%d', errors='coerce')

# Clean Amount column: remove $ and commas, convert to float
dataset['Amount'] = dataset['Amount'].replace('[\$,]', '', regex=True).astype(float)

# Check dataset structure
print("First 5 rows:")
print(dataset.head())

print("\nDataset info:")
print(dataset.info())

print("\nNumerical summary:")
print(dataset.describe())

# Check missing values
print("\nMissing values per column:")
print(dataset.isnull().sum())

# Drop duplicates
dataset = dataset.drop_duplicates()

### Quick insights

# Total sales per country
country_sales = dataset.groupby('Country')['Amount'].sum().sort_values(ascending=False)
print("\nTotal sales per country:")
print(country_sales)

# Total boxes shipped per product
product_boxes = dataset.groupby('Product')['Boxes_Shipped'].sum()
print("\nTotal boxes shipped per product:")
print(product_boxes)

# Top 5 salespersons by sales amount
top_salesperson = dataset.groupby('Sales_Person')['Amount'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 salespersons:")
print(top_salesperson)


# Chart 3: Top 5 Salespersons
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.barplot(x=top_salesperson.index, y=top_salesperson.values)
plt.title("Top 5 Salespersons by Sales Amount")
plt.ylabel("Amount")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()


