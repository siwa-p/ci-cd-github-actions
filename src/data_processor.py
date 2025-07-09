from typing import Dict, List

import pandas as pd


class DataProcessor:
    """Main data processing class."""

    def __init__(self, config: Dict):
        self.config = config
        self.processed_records = 0

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean and validate data."""
        if df.empty:
            return df
        df_clean = df.drop_duplicates()
        df_clean = df_clean.fillna(self.config.get("fill_value", 0))
        self.processed_records += len(df_clean)
        return df_clean

    def validate_schema(self, df: pd.DataFrame, required_columns: List[str]) -> bool:
        """Validate DataFrame has required columns."""
        return all(col in df.columns for col in required_columns)

    def calculate_metrics(self, df: pd.DataFrame) -> Dict:
        """Calculate data quality metrics."""
        if df.empty:
            return {"total_rows": 0, "null_percentage": 0}

        return {
            "total_rows": len(df),
            "null_percentage": (df.isnull().sum().sum() / (len(df) * len(df.columns)))
            * 100,
            "duplicate_count": df.duplicated().sum(),
        }
