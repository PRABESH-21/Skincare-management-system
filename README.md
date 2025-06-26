# skincare-management-system
Overview
The WeCare Beauty Products Management System is a Python-based console application designed to manage inventory, process sales, and handle restocking for a beauty products store. It provides a simple interface for tracking products, generating invoices, and creating purchase forms, with a focus on ease of use and data persistence through text files.

Features:

Inventory Management: Load/save product data (name, brand, quantity, cost, origin) from/to inventory.txt.
Restocking: Add stock, update prices, and generate purchase forms.
Sales: Process sales with a "Buy 3 Get 1 Free" promotion, generate invoices, and update inventory.
Input Validation: Ensures robust input handling.
Output: Creates invoices and purchase forms as text files.

File Structure:

main.py: Program entry point and menu.

read.py: Loads inventory and creates default data if needed.

operation.py: Handles restocking and sales.

write.py: Saves inventory and generates transaction files.
