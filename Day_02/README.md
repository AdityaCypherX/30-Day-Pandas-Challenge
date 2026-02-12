# 📅 Day 02 — 30 Days of Pandas Challenge

Welcome to **Day 2** of my **30 Days of Pandas Challenge** 🚀
This day focuses on practicing **real-world data filtering, joins, and self-relational logic** using Pandas.

---

## ✅ Problems Solved

### 1️⃣ 183. Customers Who Never Order

**Difficulty:** Easy
**Concepts Used:**
* Left Join (`merge`)
* Null filtering (`isna()`)
* Column selection

**Problem Statement:**
Find all customers who have **never placed any order**.
**Core Logic:**
Perform a left join between `Customers` and `Orders` and filter records where `customerId` is `NULL`.

---
### 2️⃣ 1148. Article Views I
**Difficulty:** Easy
**Concepts Used:**
* Conditional filtering
* Deduplication (`drop_duplicates()`)
* Sorting (`sort_values()`)

**Problem Statement:**
Find all authors who have **viewed at least one of their own articles**.
**Core Logic:**
Filter rows where `author_id == viewer_id`, remove duplicates, and sort results in ascending order.

---
## 🧠 Learning Outcomes (Day 2)
* Understanding **anti-join logic** in Pandas
* Working with **left joins**
* Handling **null values**
* Performing **self-condition filtering**
* Removing duplicates efficiently
* Sorting structured outputs
---
## 📂 Folder Structure

```
Day_02/
│
├── 183_Customers_Who_Never_Order.py
├── 1148_Article_Views_I.py
└── README.md
```
## 🎯 Challenge Goal
Build strong foundations in **data manipulation** using Pandas for:
* Data Analytics
* Data Science
* Machine Learning pipelines
* Real-world data projects

---📌 **Challenge:** LeetCode – 30 Days of Pandas
📅 **Day:** 02
👨‍💻 **Track:** Data Analytics / Data Science
🎯 **Focus:** Consistency + Daily Practice

---

✨ *Discipline beats motivation. Daily progress builds mastery.*

