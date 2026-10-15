.Expense Tracker

DecodeLabs Industrial Training Kit - Python Programming, Project 2 (Batch 2026)

A command-line Python script that lets a user enter expense amounts one at a time, adds them up, and displays the Total Spent.

Features
Continuous data entry using a while True loop
Accumulator pattern to keep a running total (total += new_expense)
Input validation with try/except ValueError (rejects words like ten)
Rejects negative amounts
Sentinel value (quit) to stop the program cleanly
Output kept in its own function, separate from the logic
How It Works (IPO Model)
Phase	What happens
Input	The user types an amount. The text is converted to a number with float()
Process	Valid amounts are added to total, which is initialized outside the loop so it keeps its value
Output	When the user types quit, the number of transactions and the final total are printed
Requirements
Python 3.6 or newer
How to Run
bash
python3 expense_tracker.py

On Windows, use python expense_tracker.py.

Example
=== Expense Tracker ===
Enter an expense amount (e.g. 100, 50, 20).
Type 'quit' when you are finished.

Enter expense: 100
  Added $100.00 | Running total: $100.00
Enter expense: 50
  Added $50.00 | Running total: $150.00
Enter expense: ten
Invalid Data: please enter a number or 'quit'.
Enter expense: 20
  Added $20.00 | Running total: $170.00
Enter expense: quit

Transactions recorded: 3

==============================
FINAL TOTAL: $170.00
==============================
Quality Checklist
 Stability: handles 5+ transactions
 State: total is initialized outside the loop
 Defense: catches ValueError on input
 Control: the quit kill switch prints the final total
Key Concepts Practiced
Math operations and accumulators
Loops and sentinel values
Type conversion and defensive coding
Separating logic from display
Author

Sunki Sricharan Reddy