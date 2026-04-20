def calculate_fare(distance_km, time_min):
    BASE = 10.0
    PER_KM = 3.0
    PER_MIN = 0.5
    MIN_FARE = 20.0

    fare = BASE + (distance_km * PER_KM) + (time_min * PER_MIN)
    return max(fare, MIN_FARE)

print("Welcome to the Trip Fare Calculator!")
while True:
    print("\n--- MENU ---")
    print("1. Calculate a new fare")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
            d = float(input("Enter distance (km): "))
            t = float(input("Enter time (minutes): "))
            price = calculate_fare(d, t)
            print(f"Estimated fare: {price:.2f}")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")