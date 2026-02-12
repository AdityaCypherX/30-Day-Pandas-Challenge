📘 Problem 1: Customers Who Never Order
🆔 LeetCode ID: 183
🧩 Difficulty: Easy
📚 Topic: Pandas, Joins, Filtering
📝 Problem Summary:
Find all customers who never placed any order.

🧠 Logic Used:

Left join Customers with Orders
Filter rows where customerId is NULL
Select customer names

import pandas as pd
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
merged = customers.merge(
orders,
how='left',
left_on='id',
right_on='customerId'
)
result = merged[merged['customerId'].isna()][['name']]
result.columns = ['Customers']
return result
