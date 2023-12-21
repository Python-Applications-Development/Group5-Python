# Initialize 30 parking spots as empty

parking_spots = [False] * 30
def display_Parking_Spots():
  print("Parking spots:")
  for i, spot in enumerate(parking_spots, 1):
    status = "Empty" if not spot else "Occupied"
    print(f"spot {i}: {status}")

def book_Parking_Spot(spot_number):
  if 1 <= spot_number <= 30:
    parking_spots[spot_number - 1] = True
    print(f"spot {spot_number} is booked.")    
  else:
    print("Invalid spot number. Please choose a spot between 1 and 30.")

def release_Parking_Spot(spot_number):
  if 1 <= spot_number <= 30:
    if parking_spots[spot_number - 1]:
      parking_spots[spot_number - 1] = False
      print(f"spot {spot_number} is released.")
    else:
      print(f"spot {spot_number} is already empty.")
  else:
      print("Invalid spot number. Please choose a spot between 1 and 30.")
# Main loop to manage parking
while True:
  print("\nOptions:")
  print("1. Display parking spots")
  print("2. Book a parking spot")
  print("3. Release a parking spot")
  print("4. Exit")

  choice = input("Enter your choice: ")
  if choice == "1":
    display_Parking_Spots()
  elif choice == "2":
    spot = int(input("Enter the spot number to book: "))
    book_Parking_Spot(spot)
  elif choice == "3":
    spot = int(input("Enter the spot number to release: "))
    release_Parking_Spot(spot)
  elif choice == "4":
    print("Exiting the parking system.")
    break
  else:
    print("Invalid choice. Please select a valid option.")