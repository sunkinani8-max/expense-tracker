def display_total(total):
    """Phase 3: Output (the View) - kept separate from the logic."""
    print("\n" + "=" * 30)
    print(f"FINAL TOTAL: ${total:,.2f}")
    print("=" * 30)


def main():
    # STATE: initialized OUTSIDE the loop so it persists between iterations
    total = 0
    count = 0

    print("=== Expense Tracker ===")
    print("Enter an expense amount (e.g. 100, 50, 20).")
    print("Type 'quit' when you are finished.\n")

    while True:  # The Continuous Audit loop
        raw = input("Enter expense: ").strip()

        # Kill switch: sentinel value ends the loop gracefully
        if raw.lower() == "quit":
            break

        # Phase 1: The Gatekeeper - convert string -> number safely
        try:
            new_expense = float(raw)
        except ValueError:
            print("Invalid Data: please enter a number or 'quit'.")
            continue

        # Extra validation: expenses can't be negative
        if new_expense < 0:
            print("Invalid Data: expense cannot be negative.")
            continue

        # Phase 2: The Accumulator Pattern - State(new) = State(old) + Input
        total += new_expense
        count += 1
        print(f"  Added ${new_expense:,.2f} | Running total: ${total:,.2f}")

    # Phase 3: Output
    print(f"\nTransactions recorded: {count}")
    display_total(total)


if __name__ == "__main__":
    main()