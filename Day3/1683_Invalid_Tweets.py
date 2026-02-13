# Day 3 – 30 Days of Pandas 🐼

Today’s Focus:
- Data Validation
- Conditional Transformations
- String Standardization

## 1️⃣ 1683. Invalid Tweets

**Problem:**  
Find the IDs of tweets where the content length is strictly greater than 15 characters.

### Solution
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets["content"].str.len() > 15][["tweet_id"]]
