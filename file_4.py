def calculate_trip_cost():
    kilometers = float(input("How many kilometers are you traveling? "))
    km_per_liter = float(input("What's your vehicle's fuel efficiency (km/L)? "))
    price_per_liter = float(input("What's the price of fuel per liter? $"))
    num_passengers = int(input("How many passengers (including the driver)? "))

    liters_used = kilometers / km_per_liter
    maintenance_cost = 0.02 * kilometers
    fuel_cost = price_per_liter * liters_used
    total_cost = maintenance_cost + fuel_cost

    clean_income = 0.20 * total_cost
    driver_cost = total_cost / (num_passengers + 1)
    passenger_cost = (total_cost - clean_income) / num_passengers

    print(f"Total trip cost: ${total_cost:.2f}")
    print(f"Driver's cost (including maintenance): ${driver_cost:.2f}")
    print(f"Individual passenger cost: ${passenger_cost:.2f}")

calculate_trip_cost()
