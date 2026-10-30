from config import llm
from tools.flight_search import search_flights


def flight_agent(state):

    print("\n✈️ Flight Agent started...")

    origin = state["origin"]
    destination = state["destination"]

    # Step 1: Search actual flight data
    flight_data = search_flights(
        origin,
        destination
    )

    if not flight_data["success"]:

        return {
            "flight_results": (
                "Flight search failed: "
                + str(flight_data["error"])
            ),
            "messages": ["Flight Agent: Search failed"]
        }

    flights = flight_data["flights"]

    if not flights:

        return {
            "flight_results": "No flights found.",
            "messages": ["Flight Agent: No flights found"]
        }

    # Step 2: Prepare data for the LLM
    prompt = f"""
You are an expert flight analysis agent.

Route: {origin} to {destination}

Flight data:
{flights}

Your responsibilities:

1. Identify scheduled, active and landed flights.
2. Remove duplicate recommendations.
3. Compare airlines and flight timings.
4. Recommend suitable scheduled flights.
5. Explain the advantages of each option.

STRICT RULES:

- Never invent ticket prices.
- Never claim a scheduled flight is bookable.
- Never claim an airline is cheaper without price data.
- Never invent baggage allowances.
- Clearly identify the source as AviationStack.
- Explain that flight schedules can change.
- Use UTC timestamps and clearly label them.
- Do not confuse flight duration with local arrival time.

Provide a professional flight comparison report.
""" 

    # Step 3: Ask Groq to analyze flights
    response = llm.invoke(prompt)

    # Step 4: Return results to shared state
    return {
        "flight_results": response.content,
        "messages": ["Flight Agent: Completed successfully"]
    }