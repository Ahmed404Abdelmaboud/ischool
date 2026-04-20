snacks = [
    {'name': 'banana', 'type': 'healthy', 'taste': 'sweet'},
    {'name': 'Chips', 'type': 'unhealthy', 'taste': 'salty'},
    {'name': 'Popcorn', 'type': 'healthy', 'taste': 'salty'},
    {'name': "lolypop" , 'type': 'unhealthy' , 'taste': 'sweet'}
]

while True:
    choice = input("Choose: (1) Recommend Snack (2) Quit")

    if choice == "1":
        isHealthy = input("Healthy or unhealthy? ").lower()
        taste = input("Sweet or salty? ").lower()

        found = False

        for s in snacks:
            if s["type"] == isHealthy and s["taste"] == taste:
                # Print the recommended snack
                print(f"Try: {s['name']}")
                found = True
                break

        if not found:
            print("No Snack Found!")

    elif choice == "2":
        print("Goodbye")
        break
    else:
        print("Invalid choice.")
