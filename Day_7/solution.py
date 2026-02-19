import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge employee and department tables
    merged = employee.merge(department, left_on="departmentId", right_on="id")
    
    # Find max salary per department
    max_salary = merged.groupby("name_y")["salary"].transform("max")
    
    # Filter employees with max salary in their department
    result = merged[merged["salary"] == max_salary]
    
    # Select and rename columns as required
    return result[["name_y", "name_x", "salary"]].rename(
        columns={
            "name_y": "Department",
            "name_x": "Employee",
            "salary": "Salary"
        }
    )
