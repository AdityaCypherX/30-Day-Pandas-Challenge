📘 Problem: Second Highest Salary
🆔 LeetCode ID: 176
🧩 Difficulty: Medium
📚 Topic: Pandas, Sorting, Deduplication, Ranking
📝 Problem Summary:

Find the second highest distinct salary from the Employee table.

If there is no second highest salary, return null (None in Pandas).

🧠 Logic Used:
Remove duplicate salaries
Sort salaries in descending order
Return the second value if it exists
Otherwise return Non


Pandas Solution:
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    unique_salaries = unique_salaries.sort_values(ascending=False)
    if len(unique_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    return pd.DataFrame({'SecondHighestSalary': [unique_salaries.iloc[1]]})
