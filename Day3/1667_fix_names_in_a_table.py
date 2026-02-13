1667 – Fix Names in a Table
📝 Problem Statement: Modify each name so that:
First character is uppercase
Remaining characters are lowercase

🎯 Objective
Standardize inconsistent string formatting.
💡 Approach
Use .str.capitalize() for vectorized transformation
Sort by user_id

🧠 Solution
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    return users.sort_values("user_id")
