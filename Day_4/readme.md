📅 Day 04 — 30 Days of Pandas Challenge
Welcome to Day 4 of my 30 Days of Pandas Challenge 🚀
Today’s focus was on data validation using regex and string filtering in Pandas.
✅ Problem Solved
1️⃣ 1517. Find Users With Valid E-Mails
Difficulty: Easy
Concepts Used:
Regex (Regular Expressions)
String filtering (str.match())
Boolean masking
Data validation

📝 Problem Statement
Find all users whose email addresses are valid.
A valid email must:
Start with a letter
Contain only:
Letters (a–z, A–Z)
Digits (0–9)
Underscore _
Period .
Dash -
End with the exact domain:@leetcode.com

🧠 Core Logic
Use a regex pattern to enforce:
Proper starting character
Allowed prefix characters
Correct domain validation
Filter the DataFrame using str.match() and return only valid rows.
🧠 Learning Outcomes (Day 4)
Applying Regex in Pandas
Real-world email validation logic
Advanced string filtering
Writing clean boolean conditions
Data cleaning fundamentals
📂 Folder Structure
Day_04/
│
├── 1517_Find_Users_With_Valid_Emails.py
└── README.md
🎯 Challenge Goal
Build strong foundations in data manipulation using Pandas for:
Data Analytics
Data Science
Machine Learning pipelines
Real-world data validation tasks
📌 Challenge: LeetCode – 30 Days of Pandas
📅 Day: 04
👨‍💻 Track: Data Analytics / Data Science
🎯 Focus: Regex + Data Validation
