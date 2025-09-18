from promptLLM import OpenAIClient

def main():
    pass
    url_api_ollama = "http://localhost:11434/api/generate"

    data = {
        "model": "gpt-oss:20b",
        "prompt": "Write a four-stanza poem about spring in the Eastern Republic of Uruguay. In English and Spanish.",
    }

    client = OpenAIClient(base_url=url_api_ollama)

    client.call(data)

if __name__ == "__main__":
    main()