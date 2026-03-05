import requests


def compute_seed(student_key: str) -> int:
    """Compute seed = sum(ord(ch) for ch in student_key.strip())."""
    cleaned = student_key.strip()
    return sum(ord(ch) for ch in cleaned)


def prompt_sku() -> str:
    """Prompt for SKU. Returns 'DONE' if user finishes."""
    while True:
        sku = input("SKU: ").strip()

        if sku.upper() == "DONE":
            return "DONE"

        if sku == "":
            print("Invalid SKU. Please enter a non-empty SKU.")
            continue

        return sku


def prompt_on_hand() -> int:
    """Prompt for on-hand quantity (int >= 0). Reprompts until valid."""
    while True:
        raw = input("On hand: ").strip()
        try:
            qty = int(raw)
            if qty < 0:
                print("Invalid on-hand quantity. Must be 0 or greater.")
                continue
            return qty
        except ValueError:
            print("Invalid on-hand quantity. Please enter a whole number (e.g., 0, 12).")


def main() -> None:
    # Step 1 — Student Key
    student_key = input("Student key: ")
    seed = compute_seed(student_key)

    # Step 4 — Threshold Logic
    if seed % 3 == 0:
        threshold = 15
    elif seed % 3 == 1:
        threshold = 12
    else:
        threshold = 9

    # Step 6 — Select API Term
    if seed % 2 == 0:
        spotcheck_term = "weezer"
    else:
        spotcheck_term = "drake"

    # Step 5 — Tracking counts
    total_skus = 0
    reorder_count = 0

    # Step 2 + Step 3 — SKU loop + on-hand input
    while True:
        sku = prompt_sku()
        if sku == "DONE":
            break

        on_hand = prompt_on_hand()
        total_skus += 1

        if on_hand < threshold:
            reorder_count += 1
            status = "REORDER"
        else:
            status = "OK"

        # Temporary feedback (not part of final required output)
        print(f"{sku}: {status}")

    # Step 7 + Step 8 — API Request + Exception Handling
    api_status = "OK"
    songs_returned = "N/A"  # will stay N/A if FAILED or INVALID_RESPONSE

    try:
        url = "https://itunes.apple.com/search"
        params = {"entity": "song", "limit": 5, "term": spotcheck_term}

        response = requests.get(url, params=params, timeout=10)
        data = response.json()  # could raise ValueError if not valid JSON

        # Validate expected JSON structure
        if not isinstance(data, dict):
            api_status = "INVALID_RESPONSE"
        elif "results" not in data or not isinstance(data["results"], list):
            api_status = "INVALID_RESPONSE"
        else:
            # We'll count songs in Step 9; for now just prove we got results
            songs_returned = len(data["results"])

    except requests.exceptions.RequestException:
        api_status = "FAILED"
    except ValueError:
        # response.json() failed or data malformed
        api_status = "INVALID_RESPONSE"

    # Temporary summary (we'll replace with exact required output later)
    print("\n--- Summary So Far (temporary) ---")
    print(f"Seed: {seed}")
    print(f"Threshold: {threshold}")
    print(f"SKUs entered: {total_skus}")
    print(f"Reorder flagged: {reorder_count}")
    print(f"Spotcheck term: {spotcheck_term}")
    print(f"Songs returned (temporary): {songs_returned}")
    print(f"API status: {api_status}")


if __name__ == "__main__":
    main()