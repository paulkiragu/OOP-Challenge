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
        #  the pet reduce hunger and increase happiness by use of max and min 
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)  # Hunger can't go below 0
        self.happiness = min(10, self.happiness + 1)  # Happiness can't exceed 10

    def sleep(self):
        #the pet increase energy
        print(f"{self.name} is sleeping...")
        self.energy = min(10, self.energy + 5)  # Energy can't exceed 10

    def play(self):
        # The pet playing:
        # If too tired, show a message and stop
        if self.energy <= 0:
            print(f"{self.name} is too tired to play.")
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

