📘 Problem 2: Article Views I
🆔 LeetCode ID: 1148
🧩 Difficulty: Easy
📚 Topic: Pandas, Filtering, Deduplication
📝 Problem Summary:

Find all authors who viewed at least one of their own articles.

🧠 Logic Used:
Filter where author_id == viewer_id
Remove duplicates
Sort by id

Pandas Solution:
import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
  result = views[views['author_id'] == views['viewer_id']]
  result = result[['author_id']].drop_duplicates()
  result.columns = ['id']
  return result.sort_values(by='id')
