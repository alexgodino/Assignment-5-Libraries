def compute_seed(student_key: str) -> int:
    """Compute seed = sum(ord(ch) for ch in student_key.strip())."""
    cleaned = student_key.strip()
    return sum(ord(ch) for ch in cleaned)


def prompt_item_name() -> str:
    """Prompt for item name. Returns 'DONE' if cashier ends checkout."""
    while True:
        name = input("Item name: ").strip()

        if name.upper() == "DONE":
            return "DONE"

        if name == "":
            print("Invalid item name. Please enter a non-empty name.")
            continue

        return name


def prompt_unit_price() -> float:
    """Prompt for unit price (float > 0). Reprompts until valid."""
    while True:
        raw = input("Unit price: ").strip()
        try:
            price = float(raw)
            if price <= 0:
                print("Invalid unit price. Must be greater than 0.")
                continue
            return price
        except ValueError:
            print("Invalid unit price. Please enter a number (e.g., 2.99).")


def prompt_quantity() -> int:
    """Prompt for quantity (int >= 1). Reprompts until valid."""
    while True:
        raw = input("Quantity: ").strip()
        try:
            qty = int(raw)
            if qty < 1:
                print("Invalid quantity. Must be at least 1.")
                continue
            return qty
        except ValueError:
            print("Invalid quantity. Please enter a whole number (e.g., 3).")


def main() -> None:
    # Step 1 — Student Key
    student_key = input("Student key: ")
    seed = compute_seed(student_key)

    # Step 4 — Running totals
    subtotal = 0.0
    total_units = 0

    # Step 2 + Step 3 — Item Entry Loop with Validation
    while True:
        item_name = prompt_item_name()
        if item_name == "DONE":
            break

        unit_price = prompt_unit_price()
        quantity = prompt_quantity()

        subtotal += unit_price * quantity
        total_units += quantity

    # Step 5 — Discount Logic
    if total_units >= 10 or subtotal >= 100:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    discount_amount = subtotal * discount_rate
    total_after_discount = subtotal - discount_amount

    # Step 6 — Seed-Based Member Perk
    perk_applied = False
    if seed % 2 == 1:  # odd seed
        total_after_discount -= 3.00
        perk_applied = True

    # Total may never fall below $0.00
    if total_after_discount < 0:
        total_after_discount = 0.0

    # Step 7 — Output Format (print exactly)
    print(f"Seed: {seed}")
    print(f"Units: {total_units}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: {int(discount_rate * 100)}%")
    print(f"Perk applied: {'YES' if perk_applied else 'NO'}")
    print(f"Total: ${total_after_discount:.2f}")


if __name__ == "__main__":
    main()