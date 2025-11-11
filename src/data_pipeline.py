import pandas as pd
import numpy as np
from scipy.stats import zscore

def load_data(path: str) -> pd.DataFrame:
    # Load Dataset 
    return pd.read_csv(path)

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase and replace spaces/invalid chars in column names."""
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace(r"[^\w_]", "", regex=True)
    )
    return df

def convert_timestamp(df, column='Timestamp'):
    """Convert timestamp column to datetime."""
    if column in df.columns:
        df[column] = pd.to_datetime(df[column], errors='coerce')
    return df

def detect_outliers_zscore(df, columns, threshold=3):
    """
    Adds z-score columns and counts outliers.
    Returns: dict of {column: number_of_outliers}
    """
    outlier_summary = {}
    numeric_cols = [col for col in columns if col in df.select_dtypes(include=np.number).columns]

    for col in numeric_cols:
        df[f'{col}_zscore'] = np.abs(zscore(df[col].dropna()))
        outlier_summary[col] = (df[f'{col}_zscore'] > threshold).sum()

    return df, outlier_summary

def impute_missing_median(df, columns):
    """Impute missing numeric values with median."""
    for col in columns:
        if col in df.columns and df[col].isnull().any():
            df[col].fillna(df[col].median(), inplace=True)
    return df

def save_clean_data(df, path):
    df.to_csv(path, index=False)

def drop_highly_missing(df: pd.DataFrame, threshold: float=0.5) -> pd.DataFrame:
    """Drop columns with missing fraction above threshold."""
    tol = len(df) * threshold
    return df.dropna(thresh=tol, axis=1)

def save_processed(df: pd.DataFrame, output_path: str) -> None:
    """Export cleaned DataFrame to CSV."""
    df.to_csv(output_path, index=False)