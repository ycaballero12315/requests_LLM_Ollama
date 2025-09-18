import requests
import json
from typing import Optional, Dict, Any

class OpenAIClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.__api_key = api_key
        self.__base_url = base_url
    
    @property
    def api_key(self) -> Optional[str]:
        return self.__api_key
    
    @property
    def base_url(self) -> str:
        return self.__base_url
    
    @api_key.setter
    def api_key(self, value: str):
        if value is not None and not isinstance(value, str):
            raise ValueError("API key must be a string or None.")
        self.__api_key = value
    
    @base_url.setter
    def base_url(self, value: str):
        if not isinstance(value, str) or not value.startswith("http"):
            raise ValueError("Base URL must be a valid URL string.")
        self.__base_url = value
    
    def call(self, data: Dict[str, Any], headers: Optional[Dict[str, str]] = None):

        req_headers = {"Content-Type": "application/json"}
        if self.api_key:
            req_headers["Authorization"] = f"Bearer {self.api_key}"
        if headers:
            req_headers.update(headers)

        response = requests.post(self.base_url, json=data, headers=req_headers, stream=True)

        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
            return
        
        print("Response received:")
        for line in response.iter_lines():
            if not line:
                continue
            obj = json.loads(line.decode("utf-8"))
            if "response" in obj:
                print(obj["response"], end="")
        print()



