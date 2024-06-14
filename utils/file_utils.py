
import pandas as pd
from typing import List

def load_names_from_excel(filepath: str) -> List[str]:
    """
    Load names from an Excel file.
    Args:
        filepath (str): The path to the Excel file.
    Returns:
        List[str]: A list of names.
    """
    df = pd.read_excel(filepath)
    return df['Name'].tolist()

