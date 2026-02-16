Problem:Patients With a Condition
🆔 LeetCode ID: 1527
🧩 Difficulty: Easy
📚 Topic: Pandas, String Filtering, Regex
📝 Problem Summary:
Find all patients who have Type I Diabetes, where the condition code starts with the prefix "DIAB1".


Pandas Solution:
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # DIAB1 must start a condition (start of string or after space)
    pattern = r'(^|\s)DIAB1\w*'
    
    result = patients[patients['conditions'].str.contains(pattern, na=False)]
    
    return result
