
from config import llm

print("STEP 1: Config imported successfully", flush=True)


def test_groq():
    print("STEP 2: Connecting to Groq...", flush=True)

    try:
        response = llm.invoke(
            "Reply with exactly: TripMate AI is online."
        )

        print("STEP 3: Response received!", flush=True)
        print(response.content, flush=True)

    except Exception as e:
        print("ERROR:", repr(e), flush=True)


if __name__ == "__main__":
    print("STEP 0: Script started", flush=True)
    test_groq()