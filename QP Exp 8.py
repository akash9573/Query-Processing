import pandas as pd

# Sample sales data
data = {
    'Item': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],
    'Units Sold': [10, 15, 20, 12, 25, 18, 22, 13, 16]
}

# Create a DataFrame from the sample data
sales_data = pd.DataFrame(data)

# Create a pivot table to find unit sold for each item
pivot_table = sales_data.pivot_table(index='Item', values='Units Sold', aggfunc='sum')

# Reset the column name for the pivot table
pivot_table.columns = ['Total Units Sold']

# Display the pivot table
print(pivot_table)
