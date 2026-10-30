
from config import llm


def response_agent(state):

    print("\n🧳 Final Response Agent started...")

    prompt = f"""
You are TripMate AI's final travel assistant.

The specialist agents have completed their work.

USER REQUEST:
{state.get("user_query", "")}

TRIP DETAILS:
Origin: {state.get("origin", "")}
Destination: {state.get("destination", "")}
Duration: {state.get("duration", "")}
Budget: {state.get("budget", "")}
Travelers: {state.get("travelers", "")}

FLIGHT RESEARCH:
{state.get("flight_results", "")}

HOTEL RESEARCH:
{state.get("hotel_results", "")}

ITINERARY:
{state.get("itinerary", "")}

YOUR TASK:

Create one polished travel planning report.

Include:

1. Trip overview
2. Flight recommendations
3. Hotel recommendations
4. Day-by-day itinerary
5. Budget considerations
6. Important travel tips
7. Missing information and verification checklist

IMPORTANT RULES:

- Preserve factual details from the specialist agents.
- Do not invent flight or hotel bookings.
- Do not invent prices or claim availability.
- Clearly label estimates and assumptions.
- Do not turn unverified suggestions into facts.
- Avoid repeating the same information unnecessarily.
- Make the final report easy to read.

End with a checklist of things the traveler must
confirm before booking.

"""

    response = llm.invoke(prompt)

    return {
        "final_response": response.content,
        "messages": ["Final Response Agent: Completed successfully"]
    }
