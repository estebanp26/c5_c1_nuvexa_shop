# c5_c1_nuvexa_shop
<img width="830" height="517" alt="Captura desde 2026-03-10 07-20-02" src="https://github.com/user-attachments/assets/28b475d5-9ad6-4a6f-97f1-8e68740e08b1" />

## Description
This program is a terminal-based sales registration system designed for small store administrators. Its purpose is to replace manual paper records with an automated, structured solution that calculates totals and generates a daily summary.
The system runs interactively from the command line and stores all sales data in memory during execution.
How It Works

1. The program starts and displays a welcome screen with the store name.
2. The system requests three inputs from the user: product name, unit price, and quantity sold.
3. The program multiplies the price by the quantity to calculate the total for each sale.
4. The system checks whether the product already exists in the dictionary. If it does, it adds the new quantity to the existing record. If it does not, it creates a new entry.
5. After each sale, the program prints an individual receipt with the full details of that transaction.
6. The program asks the user whether another sale needs to be registered.
7. When the user finishes, the system displays a consolidated summary showing every product sold, the total units per product, and the total revenue for the day.

## Results
The program successfully registers multiple sales in a single session and produces a clean, formatted summary at the end of the day. The dictionary structure groups repeated products automatically, which means the same product can be sold multiple times without creating duplicate entries.


## Status
>The project is currently running as a fully functional terminal application. All four modules are connected and working correctly. Future improvements could include date stamping, input validation, exporting to a text file, and other features.
