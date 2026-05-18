# RENTAL HOUSE UTILITY BILL CALCULATOR

RENT_COST = 1_200_000
ELECTRICITY_PRICE = 4000
WATER_PRICE = 10000


def calculate_electricity_usage(new_reading, old_reading):
    electricity_used = new_reading - old_reading
    electricity_cost = electricity_used * ELECTRICITY_PRICE

    print(f"Electricity consumed: {electricity_used} kWh")
    print("\n" * 3)
    print("〰️" * 8)

    return electricity_cost


def calculate_water_usage(new_reading, old_reading):
    water_used = new_reading - old_reading
    water_cost = water_used * WATER_PRICE

    print(f"Water consumed: {water_used} m3")
    print("\n" * 3)
    print("〰️" * 8)

    return water_cost


def calculate_total_bill(electricity_cost, water_cost):
    total_bill = electricity_cost + water_cost + RENT_COST

    print(f"Total electricity bill: {electricity_cost:,} VND")
    print(f"Total water bill: {water_cost:,} VND")
    print(f"Monthly rent cost: {RENT_COST:,} VND")
    print(f"Total payment: {total_bill:,} VND")


calculate_total_bill(
    electricity_cost=calculate_electricity_usage(
        new_reading=int(input("Enter new electricity meter reading: ")),
        old_reading=int(input("Enter old electricity meter reading: "))
    ),

    water_cost=calculate_water_usage(
        new_reading=int(input("Enter new water meter reading: ")),
        old_reading=int(input("Enter old water meter reading: "))
    )
)
