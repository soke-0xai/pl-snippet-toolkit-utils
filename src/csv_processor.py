"""
CSV読み込み+欠損値処理ユーティリティ
"""
import pandas as pd
import numpy as np
from typing import Optional, Union, Dict, Any
from pathlib import Path

class CSVProcessor:
    """CSV読み込みと欠損値処理のためのユーティリティクラス"""
    def __init__(self, file_path: Union[str, Path]):
        self.file_path = Path(file_path)
        self.df: Optional[pd.DataFrame] = None
    def load_csv(self, **kwargs) -> pd.DataFrame:
        try:
            self.df = pd.read_csv(self.file_path, **kwargs)
            return self.df
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")
        except Exception as e:
            raise ValueError(f"Error reading CSV: {e}")
    def get_missing_info(self) -> Dict[str, Any]:
        if self.df is None:
            raise ValueError("CSV not loaded. Call load_csv() first.")
        missing_count = self.df.isnull().sum()
        missing_percent = (missing_count / len(self.df)) * 100
        return {
            "total_rows": len(self.df),
            "missing_count": missing_count.to_dict(),
            "missing_percent": missing_percent.to_dict(),
            "columns_with_missing": missing_count[missing_count > 0].index.tolist()
        }
    def handle_missing_values(self, strategy: str = "drop", fill_value: Union[str, int, float] = None, columns: Optional[list] = None) -> pd.DataFrame:
        if self.df is None:
            raise ValueError("CSV not loaded. Call load_csv() first.")
        df_copy = self.df.copy()
        target_columns = columns or df_copy.columns.tolist()
        if strategy == "drop":
            df_copy = df_copy.dropna(subset=target_columns)
        elif strategy == "fill":
            if fill_value is None:
                for col in target_columns:
                    if df_copy[col].dtype in ['int64', 'float64']:
                        df_copy[col].fillna(df_copy[col].mean(), inplace=True)
                    else:
                        df_copy[col].fillna(df_copy[col].mode().iloc[0] if not df_copy[col].mode().empty else "unknown", inplace=True)
            else:
                df_copy[target_columns] = df_copy[target_columns].fillna(fill_value)
        elif strategy == "forward_fill":
            df_copy[target_columns] = df_copy[target_columns].fillna(method='ffill')
        elif strategy == "backward_fill":
            df_copy[target_columns] = df_copy[target_columns].fillna(method='bfill')
        elif strategy == "interpolate":
            for col in target_columns:
                if df_copy[col].dtype in ['int64', 'float64']:
                    df_copy[col] = df_copy[col].interpolate()
        else:
            raise ValueError(f"Unknown strategy: {strategy}")
        return df_copy
    def export_processed(self, output_path: Union[str, Path], df: pd.DataFrame) -> None:
        df.to_csv(output_path, index=False)
        print(f"Processed data exported to: {output_path}")

def example_usage():
    pass

if __name__ == "__main__":
    example_usage()
