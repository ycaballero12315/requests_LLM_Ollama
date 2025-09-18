import requests
import json

url_api_ollama = "http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json"
}
data = {
    "model": "gpt-oss:20b",
    "prompt": "Write a four-stanza poem about spring in the Eastern Republic of Uruguay. In English and Spanish.",
}

response = requests.post(url_api_ollama, headers=headers, json=data, stream=True)

if response.status_code == 200:
    print("\nOllama API Response:\n")
    for line in response.iter_lines():
        if line:
            obj = json.loads(line.decode("utf-8"))
            if "response" in obj:
                print(obj["response"], end="")
else:
    print(f"Error: {response.status_code} - {response.text}")
