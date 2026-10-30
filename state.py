from typing import TypedDict


class TravelState(TypedDict):

    user_query: str

    origin: str
    destination: str
    duration: str
    budget: str
    travelers: str

    flight_results: str
    hotel_results: str
    itinerary: str

    final_response: str

    messages: list[str]