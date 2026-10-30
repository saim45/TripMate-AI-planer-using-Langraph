
from tools.web_search import search_web

result = search_web(
    "Best hotels in Dubai for tourists with approximate prices and amenities",
    max_results=5
)

if result["success"]:
    print("\nSEARCH ANSWER:")
    print(result["answer"])

    print("\nSEARCH RESULTS:")

    for item in result["results"]:
        print("\nHotel / Page:", item["title"])
        print("URL:", item["url"])
        print("Information:", item["content"][:500])
else:
    print("Search failed:", result["error"])
