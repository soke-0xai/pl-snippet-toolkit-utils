"""
REST APIクライアントユーティリティ
"""
import requests
from typing import Optional, Dict, Any

class APIClient:
    """REST API通信のためのクライアント"""
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        self.base_url = base_url
        self.headers = headers or {}
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, retries: int = 3) -> Any:
        url = f"{self.base_url}{endpoint}"
        for attempt in range(retries):
            try:
                response = requests.get(url, headers=self.headers, params=params, timeout=10)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                if attempt == retries - 1:
                    raise
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, retries: int = 3) -> Any:
        url = f"{self.base_url}{endpoint}"
        for attempt in range(retries):
            try:
                response = requests.post(url, headers=self.headers, json=data, timeout=10)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                if attempt == retries - 1:
                    raise
