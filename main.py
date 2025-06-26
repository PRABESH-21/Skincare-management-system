"""
Main program for Beauty Products Management - WeCare.
"""

import datetime
from read import get_inventory_data, print_inventory
from operation import restock_items, sell_items


def display_header():
    """
    Shows the program header and current date/time.

    Parameters:
        None

    Returns:
        None
    """
    # Get current date and time
    now = datetime.datetime.now()
    date_string = "%s-%s-%s %s:%s:%s" % (now.year, now.month, now.day, now.hour, now.minute, now.second)

    # Print store information
    print("\n\n")
    print("\t" * 5 + "WeCare Beauty Products")
    print("\n")
    print("\t" * 3 + "Kamalpokhari, Kathmandu | Phone No: 9761625564")
    print("\n")
    print("-" * 80)
    print("\t" * 3 + "Welcome to the system! " + date_string)
    print("-" * 80)
    print("\n")
    print("Buy 3 Get 1 Free on all products!")
    print("\n")


def display_menu():
    """
    Shows the main program menu.

    Parameters:
        None

    Returns:
        int: Selected menu option
    """
    print("\n" + "=" * 30)
    print("MAIN MENU")
    print("=" * 30)
    print("1. Add New Stock")
    print("2. Process Sale")
    print("3. Exit Program")

    try:
        selected = int(input("Enter option number: "))
        return selected
    except:
        print("Invalid selection. Please try again.")
        return 0


def start_program():
    """
    Main function that starts the program.

    Parameters:
        None

    Returns:
        None
    """
    # Show program header
    display_header()

    # Try to load inventory
    try:
        # Load data from file
        inventory_data = get_inventory_data()

        # Display current inventory
        print_inventory(inventory_data)

        # Start program loop
        program_running = True
        while program_running:
            try:
                # Get user menu selection
                option = display_menu()

                # Process selected option
                if option == 1:
                    # Restock inventory
                    restock_items(inventory_data)

                elif option == 2:
                    # Process a sale
                    sell_items(inventory_data)

                elif option == 3:
                    # Exit program
                    print("Thank you for using WeCare Beauty Products Management")
                    program_running = False

                else:
                    print("Please select a valid option (1-3)")

            except:
                print("An error occurred while processing your request")
                print("Please try again")

    except:
        print("Fatal error starting the program")
        print("System will now exit")


# Run program when script is executed directly
if __name__ == "__main__":
    start_program()