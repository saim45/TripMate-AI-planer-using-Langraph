import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")


def search_flights(origin, destination):

    if not API_KEY:
        return {
            "success": False,
            "error": "AviationStack API key missing"
        }

    url = "https://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "dep_iata": origin.upper(),
        "arr_iata": destination.upper(),
        "limit": 20
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=20
        )

        response.raise_for_status()
        data = response.json()

        if "error" in data:
            return {
                "success": False,
                "error": data["error"]
            }

        flights = []
        seen = set()

        for flight in data.get("data", []):

            airline = flight.get("airline") or {}
            flight_info = flight.get("flight") or {}
            departure = flight.get("departure") or {}
            arrival = flight.get("arrival") or {}

            flight_number = flight_info.get("iata")

            dep_time = departure.get("scheduled")
            arr_time = arrival.get("scheduled")

            key = (flight_number, dep_time, arr_time)

            if key in seen:
                continue

            seen.add(key)

            flights.append({
                "airline": airline.get("name"),
                "flight_number": flight_number,
                "departure": dep_time,
                "arrival": arr_time,
                "status": flight.get("flight_status")
            })

        return {
            "success": True,
            "flights": flights
        }

    except requests.RequestException as e:

        return {
            "success": False,
            "error": str(e)
        }