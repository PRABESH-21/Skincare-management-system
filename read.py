"""
Inventory data loading module for WeCare Beauty system.
"""


def get_inventory_data(filename="inventory.txt"):
    """
    Loads inventory data from text file.

    Parameters:
        filename (str): Name of inventory file to read

    Returns:
        list: List of product data where index corresponds to product ID
    """
    try:
        # Open inventory file
        inventory_file = open(filename, "r")
        file_content = inventory_file.readlines()
        inventory_file.close()

        # Create inventory list
        inventory_data = []

        # Add placeholder at position 0 so IDs start at 1
        inventory_data.append(None)

        # Process each line in file
        for line_content in file_content:
            # Remove newline and split by comma
            data = line_content.replace("\n", "").split(",")

            # Clean whitespace from each item
            clean_data = []
            for item in data:
                # Remove leading space
                if len(item) > 0 and item[0] == ' ':
                    item = item[1:]
                # Remove trailing space
                if len(item) > 0 and item[-1] == ' ':
                    item = item[:-1]
                clean_data.append(item)

            # Add to inventory list
            inventory_data.append(clean_data)

        return inventory_data

    except:
        print("Inventory file '" + filename + "' not found. Creating new file with sample data.")
        create_default_inventory(filename)
        return get_inventory_data(filename)  # Try again after creating file


def create_default_inventory(filename="inventory.txt"):
    """
    Creates a new inventory file with sample data.

    Parameters:
        filename (str): Name of inventory file to create

    Returns:
        None
    """
    # Sample product data
    sample_data = [
        "Vitamin C Serum, Garnier, 200, 1000, France",
        "Skin Cleanser, Cetaphil, 100, 280, Switzerland",
        "Sunscreen, Aqualogica, 200, 700, India",
    ]

    try:
        # Create and write to file
        inventory_file = open(filename, "w")
        for product in sample_data:
            inventory_file.write(product + "\n")
        inventory_file.close()

        print("New inventory file created successfully!")
    except:
        print("Could not create inventory file")


def print_inventory(inventory_data):
    """
    Displays inventory data in a formatted table.

    Parameters:
        inventory_data (list): List of product information

    Returns:
        None
    """
    # Print table header
    print("#" * 80)
    print("ID\t\tName\t\t\tBrand\t\tQty\tCost Price\tSelling Price\tOrigin")
    print("#" * 80)

    # Print each product row
    for index in range(1, len(inventory_data)):
        try:
            product = inventory_data[index]

            # Calculate selling price (200% markup)
            cost = float(product[3])
            selling_price = cost * 3

            # Print formatted row
            print("%s\t%s\t\t%s\t\t%s\t%s\t\t%.2f\t\t%s" %
                  (str(index), product[0], product[1], product[2],
                   product[3], selling_price, product[4]))

        except:
            print("Error displaying product " + str(index))