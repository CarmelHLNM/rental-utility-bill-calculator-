# Rental Utility Bill Calculator

A simple Python tool for calculating rental house expenses, including:

- Electricity bill
- Water bill
- Monthly rent
- Total payment

## Features

- Calculate electricity usage (kWh)
- Calculate water usage (m3)
- Automatically calculate the total monthly bill
- Simple command-line interface

## Project Structure

```text
project/
├── english_version.py
├── vietnamese_version.py
└── README.md
```

## How It Works

The user enters:

- New electricity meter reading
- Old electricity meter reading
- New water meter reading
- Old water meter reading

The program then calculates:

- Electricity cost
- Water cost
- Monthly rental cost
- Total amount to pay

## Pricing Configuration

Current pricing:

- Rent: 1,200,000 VND
- Electricity: 4,000 VND / kWh
- Water: 10,000 VND / m3

You can easily modify these values in the code.

## How to Run

Run the Python file:

```bash
python english_version.py
```

## Example

```text
Enter new electric reading: 120
Enter old electric reading: 100

Electricity consumed: 20 kWh

Enter new water reading: 15
Enter old water reading: 10

Water consumed: 5 m3

Total electricity bill: 80,000 VND
Total water bill: 50,000 VND
Monthly rent: 1,200,000 VND

Total payment: 1,330,000 VND
```

## Purpose

This project was created for practicing:

- Python functions
- Variables and constants
- User input
- Basic arithmetic operations
- Code organization
