
from config import llm
from tools.web_search import search_web


# Convert common airport codes into city names for hotel searches.
AIRPORT_CITIES = {
    "DEL": "Delhi",
    "DXB": "Dubai",
    "BOM": "Mumbai",
    "BLR": "Bengaluru",
    "HYD": "Hyderabad",
    "MAA": "Chennai",
    "CCU": "Kolkata",
    "SIN": "Singapore",
    "LHR": "London",
    "JFK": "New York",
    "CDG": "Paris"
}


def hotel_agent(state):

    print("\n🏨 Hotel Agent started...")

    destination_code = state["destination"].upper()
    destination = AIRPORT_CITIES.get(
        destination_code,
        state["destination"]
    )

    duration = state.get("duration", "Not specified")
    budget = state.get("budget", "Not specified")
    travelers = state.get("travelers", "Not specified")

    query = (
        f"Best hotels and accommodation options in {destination}. "
        f"Find options for {travelers} travelers staying for {duration}. "
        f"Include hotel location, amenities, approximate prices if published, "
        f"and official booking websites."
    )

    search_data = search_web(query, max_results=7)

    if not search_data["success"]:
        return {
            "hotel_results": (
                "Hotel search failed: " + str(search_data["error"])
            ),
            "messages": ["Hotel Agent: Search failed"]
        }

    results = search_data.get("results", [])

    if not results:
        return {
            "hotel_results": "No useful hotel search results found.",
            "messages": ["Hotel Agent: No results found"]
        }

    prompt = f"""
You are TripMate AI's hotel research and recommendation agent.

TRIP DETAILS
Destination: {destination}
Duration: {duration}
Travelers: {travelers}
Overall trip budget provided by user: {budget}

WEB SEARCH ANSWER
{search_data.get("answer", "No answer provided")}

WEB SEARCH RESULTS
{results}

YOUR TASK
Analyze the supplied search results and prepare a useful hotel
recommendation report.

Follow these rules strictly:

1. Recommend hotels only when they are actually mentioned in the
   supplied search results.
2. Compare hotels using available information such as location,
   amenities, traveler suitability and published prices.
3. Include the source URL for each recommendation.
4. If prices are not available, explicitly write
   "Price not available in the retrieved sources".
5. Never invent prices, ratings, amenities, addresses or facilities.
6. Do not claim that rooms are currently available or bookable.
7. The user's budget is the overall trip budget, not necessarily
   the hotel budget. Do not assume the entire budget is for hotels.
8. If the sources are insufficient for a reliable comparison,
   clearly explain what information is missing.
9. End with a short recommendation explaining which options
   deserve further consideration.

Use clear headings and a comparison table where possible.
"""

    response = llm.invoke(prompt)

    return {
        "hotel_results": response.content,
        "messages": ["Hotel Agent: Completed successfully"]
    }
