# Rental Utility Bill Calculator

```text
Rental Utility Bill Calculator
│
**├── Project Overview**
│   ├── Simple Python rental expense calculator
│   ├── Command-line based utility billing tool
│   └── Calculates monthly rental expenses
│
├── Core Functions
│   │
│   ├── Electricity Calculation
│   │   ├── Calculate kWh usage
│   │   ├── Calculate electricity cost
│   │   └── Compare old/new meter readings
│   │
│   ├── Water Calculation
│   │   ├── Calculate water usage (m3)
│   │   ├── Calculate water bill
│   │   └── Compare old/new water readings
│   │
│   ├── Rental Cost
│   │   └── Add fixed monthly rent
│   │
│   └── Total Payment
│       ├── Combine all expenses
│       └── Display final payment amount
│
├── User Input Flow
│   │
│   ├── Electricity Meter
│   │   ├── New reading
│   │   └── Old reading
│   │
│   └── Water Meter
│       ├── New reading
│       └── Old reading
│
├── Calculation Flow
│   │
│   ├── Electricity Usage
│   │   └── new_reading - old_reading
│   │
│   ├── Water Usage
│   │   └── new_reading - old_reading
│   │
│   ├── Utility Costs
│   │   ├── electricity_usage × electricity_price
│   │   └── water_usage × water_price
│   │
│   └── Final Bill
│       └── rent + electricity + water
│
├── Pricing Configuration
│   │
│   ├── Rent
│   │   └── 1,200,000 VND
│   │
│   ├── Electricity Price
│   │   └── 4,000 VND / kWh
│   │
│   └── Water Price
│       └── 10,000 VND / m3
│
├── Project Structure
│
│   project/
│   ├── english_version.py
│   ├── vietnamese_version.py
│   └── README.md
│
├── Program Execution
│   │
│   ├── Run Command
│   │
│   │   python english_version.py
│   │
│   └── Interface Type
│       └── Command-line interface (CLI)
│
├── Example Workflow
│   │
│   ├── Electricity Input
│   │   ├── New reading: 120
│   │   └── Old reading: 100
│   │
│   ├── Water Input
│   │   ├── New reading: 15
│   │   └── Old reading: 10
│   │
│   ├── Consumption Result
│   │   ├── Electricity: 20 kWh
│   │   └── Water: 5 m3
│   │
│   └── Final Costs
│       ├── Electricity bill: 80,000 VND
│       ├── Water bill: 50,000 VND
│       ├── Rent: 1,200,000 VND
│       └── Total payment: 1,330,000 VND
│
└── Learning Purpose
    │
    ├── Python Functions
    ├── Variables & Constants
    ├── User Input Handling
    ├── Arithmetic Operations
    ├── Code Organization
    └── CLI Program Structure
```
