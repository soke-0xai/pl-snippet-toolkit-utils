"""
チャート生成ユーティリティ
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Optional, List, Dict, Any

class ChartGenerator:
    """チャート生成のためのユーティリティクラス"""
    def __init__(self, df: pd.DataFrame):
        self.df = df
    def bar_chart(self, x: str, y: str, title: str = "", save_path: Optional[str] = None) -> None:
        plt.figure(figsize=(10, 6))
        sns.barplot(x=x, y=y, data=self.df)
        plt.title(title)
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()
    def line_chart(self, x: str, y: str, title: str = "", save_path: Optional[str] = None) -> None:
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=x, y=y, data=self.df)
        plt.title(title)
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()
    def scatter_chart(self, x: str, y: str, title: str = "", save_path: Optional[str] = None) -> None:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=x, y=y, data=self.df)
        plt.title(title)
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()
