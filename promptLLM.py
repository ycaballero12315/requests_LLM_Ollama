import requests
import json
from typing import Optional, Dict, Any

class OpenAIClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.api_key = api_key
        self.base_url = base_url
    
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



