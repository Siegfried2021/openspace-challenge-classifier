import pandas as pd

def load_names_from_excel(filepath: str):
    """
    Load names from an Excel file.
    Args:
        filepath (str): The path to the Excel file.
    Returns:
        List[str]: A list of names.
    """
    df = pd.read_excel(filepath)
    return df['Colleagues'].tolist()
