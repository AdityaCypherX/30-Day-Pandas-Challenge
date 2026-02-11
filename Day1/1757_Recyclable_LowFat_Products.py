"""
Problem ID: 1757
Title: Recyclable and Low Fat Products
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Data Filtering | Boolean Indexing
"""

import pandas as pd

# Solution
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return result[['product_id']]
