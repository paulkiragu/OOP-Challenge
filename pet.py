# Define the Pet class
class Pet:
    def __init__(self, name):
        # Initialize the pet with default values
        self.name = name
        self.hunger = 5      
        self.energy = 5      
        self.happiness = 5    
        self.tricks = []     

    def eat(self):
        # Pet eats: reduce hunger and increase happiness
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)            # Hunger can't go below 0
        self.happiness = min(10, self.happiness + 1)     # Happiness can't exceed 10

    def sleep(self):
        # Pet sleeps: increase energy
        print(f"{self.name} is sleeping...")
        self.energy = min(10, self.energy + 5)           # Energy can't exceed 10

    def play(self):
        # Pet plays if not too tired or hungry
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

    def train(self, trick):
        # Teach the pet a new trick
        print(f"{self.name} is learning a new trick: {trick}!")
        self.tricks.append(trick)
        self.happiness = max(0, self.happiness - 1)      
        self.energy = max(0, self.energy - 1)            
    def show_tricks(self):
        # Display all learned tricks
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for t in self.tricks:
                print(f" - {t}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        # Show current status of the pet
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
