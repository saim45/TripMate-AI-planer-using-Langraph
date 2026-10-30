
from agents.response_agent import response_agent

state = {
    "user_query": "Plan a 5-day Dubai trip from Delhi",
    "origin": "DEL",
    "destination": "DXB",
    "duration": "5 days",
    "budget": "100000 INR",
    "travelers": "2",
    "flight_results": "Flight research output goes here.",
    "hotel_results": "Hotel research output goes here.",
    "itinerary": "Your generated itinerary goes here.",
    "final_response": "",
    "messages": []
}

result = response_agent(state)

print("\n========== FINAL TRIPMATE REPORT ==========")
print(result["final_response"])

print("\n========== AGENT STATUS ==========")
print(result["messages"])
