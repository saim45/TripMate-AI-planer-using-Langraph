from agents.flight_agent import flight_agent


# Sample shared state
state = {
    "user_query": "Find flights from Delhi to Dubai",

    "origin": "DEL",
    "destination": "DXB",
    "duration": "5 days",
    "budget": "100000 INR",
    "travelers": "2",

    "flight_results": "",
    "hotel_results": "",
    "itinerary": "",
    "final_response": "",

    "messages": []
}


result = flight_agent(state)

print("\n========== FLIGHT RECOMMENDATIONS ==========")

print(result["flight_results"])

print("\n========== EXECUTION LOG ==========")

print(result["messages"])