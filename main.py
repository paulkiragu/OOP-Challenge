from pet import Pet  # Import the Pet class from pet.py

# ---- Interacting with the Pet ----
def interact_with_pet():
    print("🐾 Welcome to the Virtual Pet Game! 🐾")

    # Ask for a pet name
    pet_name = input("What would you like to name your pet? ").strip()
    while not pet_name:
        print("Pet name cannot be empty.")
        pet_name = input("Please enter a valid name for your pet: ").strip()

    pet = Pet(pet_name)

    # Perform some actions
    pet.eat()    
    pet.play()   
    pet.sleep()  
    
    # Teach pet some tricks
    pet.train("roll over")
    pet.train("play dead")
    
    # Show the current status and tricks
    pet.get_status()
    pet.show_tricks()

# Start the interaction
if __name__ == "__main__":
    interact_with_pet()
