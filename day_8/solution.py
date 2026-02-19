import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Create a new DataFrame with required columns
    result = pd.DataFrame()
    
    # Sort by score descending
    result["score"] = scores["score"]
    
    # Dense rank (highest score = 1)
    result["rank"] = scores["score"].rank(method="dense", ascending=False)
    
    # Convert rank to integer
    result["rank"] = result["rank"].astype(int)
    
    # Return sorted result
    return result.sort_values(by="score", ascending=False)
