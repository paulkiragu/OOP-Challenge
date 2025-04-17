# Define the Pet class
class Pet:
    def __init__(self, name):
        # Initialize the class pet with a name and default values
        self.name = name
        self.hunger = 5      
        self.energy = 5      
        self.happiness = 5  
        self.tricks = []    

    def eat(self):
        # The pet reduces hunger and increases happiness
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)  # Hunger can't go below 0
        self.happiness = min(10, self.happiness + 1)  # Happiness can't exceed 10

    def sleep(self):
        # The pet increases energy
        print(f"{self.name} is sleeping...")
        self.energy = min(10, self.energy + 5)  # Energy can't exceed 10

    def play(self):
        # The pet plays:
        # If too tired or too hungry, show a message and stop
        if self.energy <= 0:
            print(f"{self.name} is too tired to play.")
            return
        if self.hunger >= 10:
            print(f"{self.name} is too hungry to play.")
            return
        
        print(f"{self.name} is playing...")
        self.energy = max(0, self.energy - 2)         
        self.happiness = min(10, self.happiness + 2)  
        self.hunger = min(10, self.hunger + 1)        

    def get_status(self):
        # Display the pet's current state
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def train(self, trick):
        # Teach the pet a new trick and store it
        print(f"{self.name} is learning a new trick: {trick}!")
        self.tricks.append(trick)
        self.happiness = max(0, self.happiness - 1)  # Training might reduce happiness slightly
        self.energy = max(0, self.energy - 1)        # Training uses up energy

    def show_tricks(self):
        # Display learned tricks
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for t in self.tricks:
                print(f" - {t}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")


# ---- Interacting with the Pet ----

def interact_with_pet():
    pet_name = input("What would you like to name your pet? ")
    pet = Pet(pet_name)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Let your pet sleep")
        print("3. Play with your pet")
        print("4. Train your pet a new trick")
        print("5. Show your pet's tricks")
        print("6. Show your pet's status")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            trick = input("Enter the trick to teach: ")
            pet.train(trick)
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.get_status()
        elif choice == "7":
            print(f"Goodbye! {pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Start the interaction
interact_with_pet()