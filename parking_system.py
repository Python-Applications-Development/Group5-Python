TOTAL_PARKING = 30


parking_spots = [{"occupied": False, "license": None} for _ in range(TOTAL_PARKING)]  


def display_parking_spots():
    print("Parking spots:")
    for i, spot in enumerate(parking_spots, 1):
        status = "Empty" if not spot["occupied"] else f"Occupied (License No: {spot['license']})"
        print(f"Spot {i}: {status}")

def book_parking_spot(spot_number, license_number):
    if 1 <= spot_number <= TOTAL_PARKING:
        if not parking_spots[spot_number - 1]["occupied"]:
            parking_spots[spot_number - 1]["occupied"] = True
            parking_spots[spot_number - 1]["license"] = license_number
            print(f"Spot {spot_number} is booked for vehicle with license plate number: {license_number}.")
        else:
            print(f"Spot {spot_number} is already occupied.")
    else:
        print("Invalid spot number. Please choose a spot between 1 and 30.")


def find_spot_by_license(license_number):
    for i, spot in enumerate(parking_spots, 1):
        if spot["occupied"] and spot["license"] == license_number:
            print(f"Vehicle with license number {license_number} is parked at spot {i}.")
            return
    print(f"No vehicle with license number {license_number} found in the parking lot.")

def release_parking_spot(spot_number):
    if 1 <= spot_number <= TOTAL_PARKING:
        if parking_spots[spot_number - 1]:
            parking_spots[spot_number - 1] = False
            print(f"spot {spot_number} is released.")
        else:
            print(f"spot {spot_number} is already empty.")
    else:
        print("Invalid spot number. Please choose a spot between 1 and 30.")

def display_parking_status():
    occupied_spots = sum(parking_spots)
    empty_spots = TOTAL_PARKING - occupied_spots
    print(f"Occupied spots: {occupied_spots}")
    print(f"Empty spots: {empty_spots}")


#Main loop to manage parking
while True:
    print("\nOptions:")
    print("1. Display parking spots")
    print("2. Book a parking spot")
    print("3. Release a parking spot")
    print("4. Find spot by license plate number")  # New option
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        display_parking_spots()
    elif choice == "2":
        spot = int(input("Enter the spot number to book: "))
        license_number = input("Enter the vehicle license plate number: ")
        book_parking_spot(spot, license_number)
    elif choice == "3":
        spot = int(input("Enter the spot number to release: "))
        release_parking_spot(spot)

  
    elif choice == "4":
        license_number = input("Enter the vehicle license plate number: ")
        find_spot_by_license(license_number)  # New functionality
    elif choice == "5":
        print("Exiting the parking system.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
