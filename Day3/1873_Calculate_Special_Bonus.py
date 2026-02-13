1873 – Calculate Special Bonus
📝 Problem Statement:calculate bonus for each employee:

🎯 Objective
Apply conditional transformation using multiple business rules.
💡 Approach
Use modulo operator for odd check
Use .str.startswith() for string condition
Apply boolean mask
Assign values using .loc[]

🧠 Solution
import pandas as pd
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (
        (employees["employee_id"] % 2 == 1) &
        (~employees["name"].str.startswith("M"))
    )

    employees["bonus"] = 0
    employees.loc[mask, "bonus"] = employees["salary"]

    return employees[["employee_id", "bonus"]].sort_values("employee_id")
