"""
File writing module for the WeCare Beauty System.
Handles inventory updates and document generation.
"""

import datetime
import random


def save_inventory(inventory_data, filename="inventory.txt"):
    """
    Saves inventory data to file.

    Parameters:
        inventory_data (list): List of product information
        filename (str): Name of file to save to

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Open file for writing
        file = open(filename, "w")

        # Write each product (skip index 0)
        for idx in range(1, len(inventory_data)):
            product = inventory_data[idx]

            # Build line from product data
            line = ""
            for i, field in enumerate(product):
                line += field
                if i < len(product) - 1:
                    line += ", "

            # Write to file
            file.write(line + "\n")

        # Close file
        file.close()
        print("Inventory file updated!")
        return True

    except:
        print("Error saving inventory data")
        return False


def generate_invoice(customer_name, phone_number, items_sold, inventory_data):
    """
    Creates a sales invoice and updates inventory.

    Parameters:
        customer_name (str): Customer name
        phone_number (str): Customer contact number
        items_sold (list): List of items in the sale
        inventory_data (list): Master inventory list

    Returns:
        str: Name of generated invoice file
    """
    # Generate date and time strings
    current = datetime.datetime.now()
    date_str = "%s-%s-%s" % (current.year, current.month, current.day)
    time_str = "%s%s%s" % (current.hour, current.minute, current.second)

    # Create unique invoice number
    invoice_num = "INV-" + str(random.randint(1000, 9999))

    # Create filename
    name_for_file = ""
    for c in customer_name:
        if c == ' ':
            name_for_file += '_'
        else:
            name_for_file += c

    filename = invoice_num + "_" + name_for_file + "_" + date_str + "_" + time_str + ".txt"

    # Initialize totals
    total_amount = 0
    shipping_fee = 0

    try:
        # Create invoice file
        file = open(filename, "w")

        # Write header
        file.write("\t \t \t \t WeCare BEAUTY PRODUCTS\n")
        file.write("\t \t Kamalpokhari, Kathmandu | Phone No: 9761625564\n")
        file.write("=" * 80 + "\n\n")
        file.write("Invoice Number: " + invoice_num + "\n")
        file.write("Date: " + date_str + "\n")
        file.write("Customer Name: " + customer_name + "\n")
        file.write("Phone Number: " + phone_number + "\n\n")
        file.write("-" * 80 + "\n")
        file.write("%-15s %-15s %-5s %-5s %-10s %-10s\n" %
                   ("Product", "Brand", "Qty", "Free", "Price", "Amount"))
        file.write("-" * 80 + "\n")

        # Print to screen as well
        print("\n\t \t \t \t WeCare BEAUTY PRODUCTS")
        print("\t \t Kamalpokhari, Kathmandu | Phone No: 9761625564")
        print("=" * 80 + "\n")
        print("Invoice Number: " + invoice_num)
        print("Date: " + date_str)
        print("Customer Name: " + customer_name)
        print("Phone Number: " + phone_number + "\n")
        print("-" * 80)
        print("%-15s %-15s %-5s %-5s %-10s %-10s" %
              ("Product", "Brand", "Qty", "Free", "Price", "Amount"))
        print("-" * 80)

        # Process each sold item
        for item in items_sold:
            product_id = item["id"]
            qty = item["quantity"]

            # Get product details
            product = inventory_data[product_id]
            name = product[0]
            brand = product[1]
            stock = int(product[2])
            cost = float(product[3])

            # Calculate promotion
            free_qty = qty // 3

            # Calculate price and amount
            price = cost * 3  # 200% markup
            amount = price * qty
            total_amount += amount

            # Write to file
            file.write("%-15s %-15s %-5s %-5s %-10s %-10s\n" %
                       (name, brand, str(qty), str(free_qty),
                        str(round(price, 2)), str(round(amount, 2))))

            # Print to screen
            print("%-15s %-15s %-5s %-5s %-10s %-10s" %
                  (name, brand, str(qty), str(free_qty),
                   str(round(price, 2)), str(round(amount, 2))))

            # Update inventory
            new_stock = stock - (qty + free_qty)
            inventory_data[product_id][2] = str(new_stock)

        # Ask about shipping
        shipping_input = input("\nDo you want your products to be shipped? (Y/N): ")
        if shipping_input.upper() == "Y":
            shipping_fee = 500
            file.write("%-45s %s\n" % ("Shipping Cost:", str(round(shipping_fee, 2))))
            print("%-45s %s" % ("Shipping Cost:", str(round(shipping_fee, 2))))

        # Calculate grand total
        grand_total = total_amount + shipping_fee

        # Write totals
        file.write("-" * 80 + "\n")
        file.write("%-45s %s\n" % ("Total Amount:", str(round(grand_total, 2))))
        file.write("=" * 80 + "\n")
        file.write("\nThank you for shopping with us!\n")
        file.write("Buy 3 Get 1 Free on all products!\n")
        file.close()

        # Print totals to screen
        print("-" * 80)
        print("%-45s %s" % ("Total Amount:", str(round(grand_total, 2))))
        print("=" * 80)
        print("\nThank you for shopping with us!")
        print("Buy 3 Get 1 Free on all products!")

        print("\nInvoice generated: " + filename)

        # Update inventory file
        save_inventory(inventory_data)
        return filename

    except:
        print("Error generating invoice")
        return None


def generate_purchase_form(supplier_name, items_purchased, inventory_data):
    """
    Creates a purchase form and updates inventory.

    Parameters:
        supplier_name (str): Supplier name
        items_purchased (list): List of items purchased
        inventory_data (list): Master inventory list

    Returns:
        str: Name of generated purchase form file
    """
    # Generate date and time strings
    current = datetime.datetime.now()
    date_str = "%s-%s-%s" % (current.year, current.month, current.day)
    time_str = "%s%s%s" % (current.hour, current.minute, current.second)

    # Create unique form number
    form_num = "PO-" + str(random.randint(1000, 9999))

    # Create filename
    name_for_file = ""
    for c in supplier_name:
        if c == ' ':
            name_for_file += '_'
        else:
            name_for_file += c

    filename = form_num + "_" + name_for_file + "_" + date_str + "_" + time_str + ".txt"

    # Initialize total
    total_amount = 0

    try:
        # Create purchase form file
        file = open(filename, "w")

        # Write header
        file.write("\t \t \t \t WeCare BEAUTY PRODUCTS\n")
        file.write("\t \t \t \t PURCHASE FORM\n")
        file.write("=" * 80 + "\n\n")
        file.write("Form Number: " + form_num + "\n")
        file.write("Date: " + date_str + "\n")
        file.write("Supplier: " + supplier_name + "\n\n")
        file.write("-" * 80 + "\n")
        file.write("%-15s %-15s %-5s %-10s %-10s\n" %
                   ("Product", "Brand", "Qty", "Cost Price", "Amount"))
        file.write("-" * 80 + "\n")

        # Print to screen as well
        print("\n\t \t \t \t WeCare BEAUTY PRODUCTS")
        print("\t \t \t \t PURCHASE FORM")
        print("=" * 80 + "\n")
        print("Form Number: " + form_num)
        print("Date: " + date_str)
        print("Supplier: " + supplier_name + "\n")
        print("-" * 80)
        print("%-15s %-15s %-5s %-10s %-10s" %
              ("Product", "Brand", "Qty", "Cost Price", "Amount"))
        print("-" * 80)

        # Process each purchased item
        for item in items_purchased:
            product_id = item["id"]
            qty = item["quantity"]
            new_cost = item.get("new_cost", None)

            # Get product details
            product = inventory_data[product_id]
            name = product[0]
            brand = product[1]
            stock = int(product[2])

            # Update cost if provided
            if new_cost:
                product[3] = str(new_cost)

            cost = float(product[3])
            amount = cost * qty
            total_amount += amount

            # Write to file
            file.write("%-15s %-15s %-5s %-10s %-10s\n" %
                       (name, brand, str(qty), str(round(cost, 2)),
                        str(round(amount, 2))))

            # Print to screen
            print("%-15s %-15s %-5s %-10s %-10s" %
                  (name, brand, str(qty), str(round(cost, 2)),
                   str(round(amount, 2))))

            # Update inventory
            new_stock = stock + qty
            inventory_data[product_id][2] = str(new_stock)

        # Write total
        file.write("-" * 80 + "\n")
        file.write("%-45s %s\n" % ("Total Amount:", str(round(total_amount, 2))))
        file.write("=" * 80 + "\n")
        file.close()

        # Print total to screen
        print("-" * 80)
        print("%-45s %s" % ("Total Amount:", str(round(total_amount, 2))))
        print("=" * 80)

        print("\nPurchase form generated: " + filename)

        # Update inventory file
        save_inventory(inventory_data)
        return filename

    except:
        print("Error generating purchase form")
        return None