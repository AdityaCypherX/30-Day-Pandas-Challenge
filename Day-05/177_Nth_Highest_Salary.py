Problem 2: Nth Highest Salary
🆔 LeetCode ID: 177
🧩 Difficulty: Medium
📚 Topic: Pandas, Sorting, Deduplication, Ranking
📝 Problem Summary:
Find the nth highest distinct salary from the Employee table.
If there are fewer than n distinct salaries, return null.

Pandas Solution:
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Get distinct salaries and sort descending, reset index
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    
    # Handle invalid N (too large or <=0)
    if N <= 0 or N > len(distinct_salaries):
        nth_salary = None
    else:
        nth_salary = distinct_salaries.iloc[N-1]  # Use .iloc for position-based indexing
    
    # Return in required format
    return pd.DataFrame({'getNthHighestSalary({})'.format(N): [nth_salary]})
