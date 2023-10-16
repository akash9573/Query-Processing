import pandas as pd

# Sample sales data
data = {
    'Item': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],
    'Sale': [100, 150, 200, 120, 250, 180, 220, 130, 160]
}

# Create a DataFrame from the sample data
sales_data = pd.DataFrame(data)

# Create a pivot table to find maximum and minimum sale values for each item
pivot_table = sales_data.pivot_table(index='Item', values='Sale', aggfunc={'Sale': ['max', 'min']})

# Reset column names for the pivot table
pivot_table.columns = ['Max Sale', 'Min Sale']

# Display the pivot table
print(pivot_table)
