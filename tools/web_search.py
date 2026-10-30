
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


def search_web(query, max_results=5):

    if not TAVILY_API_KEY:
        return {
            "success": False,
            "error": "TAVILY_API_KEY missing in .env"
        }

    url = "https://api.tavily.com/search"

    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "basic",
        "max_results": max_results,
        "include_answer": True
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        results = []

        for item in data.get("results", []):
            results.append({
                "title": item.get("title"),
                "url": item.get("url"),
                "content": item.get("content")
            })

        return {
            "success": True,
            "answer": data.get("answer", ""),
            "results": results
        }

    except requests.RequestException as e:
        return {
            "success": False,
            "error": str(e)
        }
