
from agents.hotel_agent import hotel_agent

state = {
    "user_query": "Find flights and hotels from Delhi to Dubai",
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

result = hotel_agent(state)

print("\n========== HOTEL RECOMMENDATIONS ==========")
print(result["hotel_results"])

print("\n========== AGENT STATUS ==========")
print(result["messages"])
