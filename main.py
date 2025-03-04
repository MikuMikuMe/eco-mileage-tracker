Certainly! Below is a Python program for "Eco-Mileage-Tracker," which helps individuals and businesses monitor and optimize their vehicle's fuel consumption to reduce their carbon footprint and fuel expenses. The program stores the data in a simple text file to keep track of fuel usage and provides functionalities to add new entries, calculate efficiency, and display statistics.

```python
import os

DATA_FILE = 'mileage_data.txt'

def load_data():
    """Load mileage data from a file."""
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, 'r') as file:
            data = file.readlines()
        return [tuple(line.strip().split(',')) for line in data]
    except IOError:
        print("Error reading data file.")
        return []

def save_data(data):
    """Save mileage data to a file."""
    try:
        with open(DATA_FILE, 'w') as file:
            for entry in data:
                file.write(','.join(entry) + '\n')
    except IOError:
        print("Error writing to data file.")

def add_entry(date, miles, gallons):
    """Add a new mileage entry."""
    data = load_data()
    data.append((date, str(miles), str(gallons)))
    save_data(data)

def calculate_efficiency():
    """Calculate and print fuel efficiency statistics."""
    data = load_data()
    
    if not data:
        print("No data available.")
        return
    
    total_miles = sum(float(entry[1]) for entry in data)
    total_gallons = sum(float(entry[2]) for entry in data)

    try:
        efficiency = total_miles / total_gallons
        print(f"Total Miles: {total_miles:.2f}")
        print(f"Total Gallons Used: {total_gallons:.2f}")
        print(f"Overall Fuel Efficiency: {efficiency:.2f} MPG")
    except ZeroDivisionError:
        print("Error: Division by zero encountered in efficiency calculation.")

def display_entries():
    """Display all mileage entries."""
    data = load_data()
    if not data:
        print("No entries to display.")
        return

    print("Date       | Miles | Gallons")
    print("----------------------------")
    for entry in data:
        print(f"{entry[0]} | {entry[1]} | {entry[2]}")

def main():
    """Main function to interact with the user."""
    while True:
        print("\nEco-Mileage Tracker")
        print("1. Add New Entry")
        print("2. Calculate Efficiency")
        print("3. Display All Entries")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                miles = float(input("Enter miles driven: "))
                gallons = float(input("Enter gallons used: "))
                add_entry(date, miles, gallons)
                print("Entry added successfully.")
            except ValueError:
                print("Invalid input. Please enter numerical values for miles and gallons.")
        
        elif choice == '2':
            calculate_efficiency()
        
        elif choice == '3':
            display_entries()
        
        elif choice == '4':
            print("Exiting the Eco-Mileage Tracker.")
            break
        else:
            print("Invalid option. Please choose an option from the menu.")

if __name__ == "__main__":
    main()
```

### Explanation:
- **Data Handling:** The program stores mileage data in a text file, `mileage_data.txt`. Each entry contains the date (string), miles driven (float), and gallons used (float).
- **Functions:** 
  - `load_data()` reads data from the file.
  - `save_data()` writes data to the file.
  - `add_entry()` allows the user to add a new entry of vehicle usage.
  - `calculate_efficiency()` calculates and displays overall fuel efficiency.
  - `display_entries()` lists all the entered records.
- **Main Loop:** Presents a menu for interacting with the program, allowing users to add data, calculate efficiency, or view all entries, with input validation and error handling to manage potential issues.
- **Error Handling:** Catches file errors and input errors, notifying users appropriately.