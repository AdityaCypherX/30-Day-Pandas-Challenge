Problem 4: Find Users With Valid E-Mails
 LeetCode ID: 1517
 Difficulty: Easy
 Topic: Pandas, Regex, String Filtering
 Problem Summary:
Find all users whose email addresses are valid.
A valid email must:
Start with a letter
Contain only allowed characters (letters, digits, _, ., -)
End with @leetcode.com

🧠 Logic Used:
Apply regex pattern using str.match()
Ensure prefix starts with a letter
Filter rows ending with @leetcode.com
Return the filtered DataFrame

pandas solution:
import pandas as pd
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    
    valid_users = users[users['mail'].str.match(pattern)]
    
    return valid_users
