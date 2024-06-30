def calculate_trip_cost():
    kilometers = float(input("How many kilometers are you traveling? "))
    km_per_liter = float(input("What's your vehicle's fuel efficiency (km/L)? "))
    price_per_liter = float(input("What's the price of fuel per liter? $"))

    liters_used = kilometers / km_per_liter
    maintenance_cost = 0.02 * kilometers
    fuel_cost = price_per_liter * liters_used
    total_cost = maintenance_cost + fuel_cost

    print(f"Your trip will cost you ${total_cost:.2f}.")
    print(f"However, ${maintenance_cost:.2f} will be the long-term maintenance cost, which you won't pay immediately.")
    print(f"That leaves your trip costing you ${fuel_cost:.2f} immediately in fuel.")

calculate_trip_cost()
