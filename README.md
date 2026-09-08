# python-project-2
A simple Python Expense Tracker that allows users to enter multiple expense amounts, calculates the total spending using accumulator logic, and displays the total amount spent. This project demonstrates basic Python input, mathematical operations, loops, and data processing.
# 💰 Expense Tracker — Python Programming (Project 2)

A simple command-line Expense Tracker built as **Project 2** of the
DecodeLabs Python Programming Industrial Training (Batch 2026).

This project focuses on **data processing and accumulation** — taking
continuous numeric input from a user and calculating a running total,
before moving on to more complex financial logic later in the track.

## ✨ Features

- ➕ Keep entering expenses one after another
- 🔢 Running total updates after every entry
- 🛑 Type `done` anytime to stop entering expenses
- ⚠️ Handles invalid input (like text instead of numbers) without crashing
- 📋 Shows a full list of all expenses entered
- 📊 Calculates the average expense at the end

## 🚀 How to Run

```bash
python3 expense_tracker.py
```

Example run:

```
Expense Tracker
---------------
Enter expense amount (or type 'done' to stop): 100
Added Rs.100.0. Current total: Rs.100.0
Enter expense amount (or type 'done' to stop): 50
Added Rs.50.0. Current total: Rs.150.0
Enter expense amount (or type 'done' to stop): done

---------------
All your expenses:
1. Rs.100.0
2. Rs.50.0

Total Spent: Rs.150.0
Average expense: Rs.75.00
```

## 🧠 Concepts Used

| Concept            | Where it's used                                    |
|--------------------|------------------------------------------------------|
| Loops (`while`)    | Keeps asking for expenses until the user stops        |
| Accumulator        | `total += expense` builds up the sum                  |
| Functions          | `get_expense()`, `main()`                              |
| Exception handling | `try/except ValueError` for invalid input              |
| Type casting       | Converting text input into `float`                     |

## 📂 Project Structure

```
expense-tracker-python/
├── expense_tracker.py
├── README.md
└── .gitignore
```

## 🏢 About

Built as part of the **DecodeLabs Industrial Training Kit — Python
Programming, Batch 2026**.

🌐 www.decodelabs.tech

