📅 Day 05 — 30 Days of Pandas Challenge
Welcome to Day 5 of my 30 Days of Pandas Challenge 🚀
Today focused on string pattern filtering and ranking logic using Pandas.
✅ Problems Solved
1️⃣ 1527. Patients With a Condition
Difficulty: Easy
Concepts Used:
String filtering
Pattern matching (str.contains())
Regex word boundary
Problem Statement:
Find patients who have Type I Diabetes, where the condition code starts with "DIAB1".
Core Logic:
Filter rows where conditions contains a word starting with DIAB1 using regex:
r'\bDIAB1'

2️⃣ 177. Nth Highest Salary
Difficulty: Medium
Concepts Used:
Sorting:Removing duplicates (drop_duplicates())
Indexing
Conditional return

Problem Statement:
Find the nth highest distinct salary.
If fewer than n distinct salaries exist, return None.
Core Logic:
 Remove duplicate salaries
 Sort in descending order
 Return nth value if exists

🧠 Learning Outcomes (Day 5)
Regex-based condition filtering
Working with space-separated string data
Ranking & distinct value extraction
Handling edge cases (null return)

📂 Folder Structure
Day_05/
│
├── 1527_Patients_With_a_Condition.py
├── 177_Nth_Highest_Salary.py
└── README.md

📌 Challenge: LeetCode – 30 Days of Pandas
📅 Day: 05
👨‍💻 Track: Data Analytics / Data Science
🎯 Focus: Pattern Matching + Ranking Logic
