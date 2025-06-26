"""
Operations module for handling sales and restocking in WeCare Beauty System.
"""

from write import generate_purchase_form, generate_invoice


def check_input(prompt_message, input_type="int", min_val=None, max_val=None):
    """
    Gets and validates user input.

    Parameters:
        prompt_message (str): Message to show user
        input_type (str): Type of input expected (int, float, str)
        min_val: Minimum acceptable value
        max_val: Maximum acceptable value

    Returns:
        Validated input value in appropriate type
    """
    while True:
        try:
            # Get input
            raw_input = input(prompt_message)

            # Check input type
            if input_type == "int":
                # Convert to integer
                value = int(raw_input)

                # Check range
                if min_val is not None and value < min_val:
                    print("Value must be at least " + str(min_val))
                    continue
                if max_val is not None and value > max_val:
                    print("Value must be at most " + str(max_val))
                    continue
                return value

            elif input_type == "float":
                # Convert to float
                value = float(raw_input)

                # Check range
                if min_val is not None and value < min_val:
                    print("Value must be at least " + str(min_val))
                    continue
                if max_val is not None and value > max_val:
                    print("Value must be at most " + str(max_val))
                    continue
                return value

            elif input_type == "str":
                # Check for empty string
                if raw_input == "":
                    print("Input cannot be empty")
                    continue
                return raw_input

            else:
                print("Unknown input type: " + input_type)
                continue

        except:
            print("Invalid input. Please provide a valid " + input_type)


def restock_items(inventory_data):
    """
    Handles restocking products from suppliers.

    Parameters:
        inventory_data (list): List of product information

    Returns:
        bool: True if completed successfully, False otherwise
    """
    print("\n" + "=" * 40)
    print("ADD NEW STOCK")
    print("=" * 40)

    try:
        # Get supplier details
        supplier_name = check_input("Enter supplier name: ", "str")

        # List to track items being restocked
        restock_list = []

        # Process multiple items
        continue_adding = "y"
        while continue_adding.lower() == "y":
            # Show available products
            print("\nCurrent products:")
            for idx in range(1, len(inventory_data)):
                product = inventory_data[idx]
                print("%d. %s (%s) - Stock: %s - Cost: %s" %
                      (idx, product[0], product[1], product[2], product[3]))

            # Get product to restock
            max_id = len(inventory_data) - 1
            product_id = check_input("\nEnter product ID to restock: ", "int", 1, max_id)

            # Get quantity
            quantity = check_input("Enter quantity to add: ", "int", 1)

            # Ask about price change
            change_price = check_input("Update cost price? (y/n): ", "str")
            new_cost = None

            if change_price.lower() == "y":
                new_cost = check_input("Enter new cost price: ", "float", 0.01)

            # Add to restock list
            restock_list.append({
                "id": product_id,
                "quantity": quantity,
                "new_cost": new_cost
            })

            # Ask if more items
            continue_adding = check_input("Add more items? (y/n): ", "str")

        # Generate purchase form if items were added
        if restock_list:
            generate_purchase_form(supplier_name, restock_list, inventory_data)
            print("Stock update completed successfully!")
            return True
        else:
            print("No items were added to stock.")
            return False

    except:
        print("Error during restocking process")
        return False


def sell_items(inventory_data):
    """
    Handles product sales to customers.

    Parameters:
        inventory_data (list): List of product information

    Returns:
        bool: True if completed successfully, False otherwise
    """
    print("\n" + "=" * 40)
    print("PROCESS SALE")
    print("=" * 40)

    try:
        # Get customer details
        customer_name = check_input("Enter customer name: ", "str")
        contact_number = check_input("Enter phone number: ", "str")

        # List to track items being sold
        sale_list = []

        # Process multiple items
        continue_adding = "y"
        while continue_adding.lower() == "y":
            # Show available products with prices
            print("\nProducts available:")
            for idx in range(1, len(inventory_data)):
                product = inventory_data[idx]
                # Calculate selling price
                cost = float(product[3])
                price = cost * 3  # 200% markup

                print("%d. %s (%s) - Price: $%.2f - Stock: %s" %
                      (idx, product[0], product[1], price, product[2]))

            # Get product to sell
            max_id = len(inventory_data) - 1
            product_id = check_input("\nEnter product ID to sell: ", "int", 1, max_id)

            # Show current stock
            stock = int(inventory_data[product_id][2])
            print("Available stock: " + str(stock))

            # Get quantity
            quantity = check_input("Enter quantity to sell: ", "int", 1)

            # Calculate promotional items
            free_items = quantity // 3
            total_needed = quantity + free_items

            # Check if enough stock
            if total_needed > stock:
                print("Not enough stock! You need " + str(total_needed) +
                      " units (" + str(quantity) + " paid + " +
                      str(free_items) + " free), but only " +
                      str(stock) + " available.")
                print("Please select a different quantity or product.")
                continue

            # Add to sale list
            sale_list.append({
                "id": product_id,
                "quantity": quantity
            })

            # Show promotional info
            print("Customer gets " + str(free_items) + " free items with this purchase!")

            # Ask if more items
            continue_adding = check_input("Add more items? (y/n): ", "str")

        # Generate sale invoice if items were sold
        if sale_list:
            generate_invoice(customer_name, contact_number, sale_list, inventory_data)
            print("Sale completed successfully!")
            return True
        else:
            print("No items were sold.")
            return False

    except:
        print("Error during sales process")
        return False