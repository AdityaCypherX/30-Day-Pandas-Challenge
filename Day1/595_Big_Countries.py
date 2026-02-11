"""
Problem ID: 595
Title: Big Countries
Platform: LeetCode
Difficulty: Easy
Topic: Pandas | Data Filtering | Boolean Indexing
"""

import pandas as pd

# Solution
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    result = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return result[['name', 'population', 'area']]
