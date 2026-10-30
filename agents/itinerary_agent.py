
from config import llm


def itinerary_agent(state):

    print("\n🗺️ Itinerary Agent started...")

    origin = state["origin"]
    destination = state["destination"]
    duration = state["duration"]
    budget = state["budget"]
    travelers = state["travelers"]

    flight_results = state.get(
        "flight_results",
        "No flight information available."
    )

    hotel_results = state.get(
        "hotel_results",
        "No hotel information available."
    )

    
    prompt = f"""
You are TripMate AI's evidence-aware travel itinerary planner.

TRIP DETAILS
Origin: {origin}
Destination: {destination}
Duration: {duration}
Budget: {budget}
Travelers: {travelers}

FLIGHT RESEARCH
{flight_results}

HOTEL RESEARCH
{hotel_results}

Create a practical day-by-day itinerary.

STRICT RELIABILITY RULES:

1. Never invent confirmed flight numbers, departure times,
   arrival times, hotel bookings or room availability.
2. Never assume breakfast or other facilities are included.
3. Do not invent exact attraction ticket prices, restaurant
   prices, taxi fares or transport fares.
4. Do not present estimated travel times as verified facts.
5. Do not assume a particular hotel has been selected.
6. If flight or hotel information is missing, state that
   clearly and plan using reasonable assumptions.
7. Separate information into:
   - Retrieved information
   - Planning suggestions
   - Unverified estimates and assumptions
8. Do not provide immigration or visa guarantees.
   Tell travelers to verify current entry requirements.
9. Avoid overcrowding the daily schedule.
10. Do not fabricate citations or source URLs.

OUTPUT FORMAT:

# Trip Overview

# Day 1 — Arrival
Morning, Afternoon, Evening

# Day 2
Morning, Afternoon, Evening

Continue for all trip days.

# Estimated Budget Considerations
Do not invent prices. Identify cost categories
that the traveler should verify.

# Important Travel Tips

# Verified Information
List what the supplied research actually confirms.

# Assumptions and Missing Information
List what still needs confirmation.
"""

    response = llm.invoke(prompt)

    return {
        "itinerary": response.content,
        "messages": ["Itinerary Agent: Completed successfully"]
    }
