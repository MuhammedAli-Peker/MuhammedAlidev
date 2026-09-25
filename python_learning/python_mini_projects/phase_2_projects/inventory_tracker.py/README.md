# Inventory Tracker

A simple command-line inventory (lost item) tracker built in Python. It allows users to add, view, update, and delete items in a personal inventory, with each item stored as a dictionary inside a list.

## Features

- **Add items** — Store item details including name, category, situation, place, and price.
- **View inventory** — Display all items in a clean, readable format.
- **Update items** — Select an item and modify any of its fields (name, category, place, price, situation).
- **Delete items** — Remove an item from the inventory by its number.
- **Input validation** — Handles invalid numeric input and out-of-range selections gracefully.

## How It Works

The inventory is stored as a **list of dictionaries**, where each dictionary represents one item:

```python
{
    "name": "laptop",
    "category": "electronics",
    "situation": "existing",
    "place": "home",
    "price": 799.99
}
```

Functions operate on this list by index, using Python's reference semantics to update items in place without needing to reassign or copy data.

## Project Structure

```
inventory_tracker.py   # Main program file
```

## Functions Overview

| Function            | Description                                              |
|----------------------|-----------------------------------------------------------|
| `get_username()`     | Prompts the user for a username (max 16 characters).      |
| `check_list()`       | Displays all items in the inventory in a readable format. |
| `check_item()`       | Lets the user view an item and optionally update it.      |
| `update_item()`      | Updates a specific field of a selected item.               |
| `add_items()`        | Adds a new item to the inventory.                          |
| `delete_items()`     | Removes an item from the inventory.                        |
| `exit_button()`      | Displays a farewell message when exiting the program.      |
| `main()`             | Runs the main menu loop and connects all functions.         |

## Getting Started

### Requirements

- Python 3.x (no external libraries required)

### Running the Program

```bash
python inventory_tracker.py
```

### Usage

1. Enter a username to begin.
2. Choose an option from the menu:
   - `1` — Check list
   - `2` — Add items
   - `3` — Delete items
   - `4` — Check items (view/update)
   - `5` — Exit the program
3. Follow the prompts to manage your inventory.

## Example

```
---Inventory List---

1. Laptop
   Category : Electronics
   Situation: Existing
   Place    : Home
   Price    : 799.99
```

## Notes

- All item data is stored in memory; the inventory resets each time the program is run (no file/database persistence yet).
- Input is validated for numeric fields (e.g., price) and menu selections.

## Author

Built by Ali as part of a self-directed Python learning journey, progressing from fundamentals toward object-oriented programming.
