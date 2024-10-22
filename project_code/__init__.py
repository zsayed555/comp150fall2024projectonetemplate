# Assuming the Statistic class is already defined like this:
class Statistic:
    def __init__(self, name: str, value: int = 10, description: str = ""):
        self.name = name
        self.value = value
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.value} ({self.description})"

# Character class
class Character:
    def __init__(self, name: str = "Bob"):
        self.name = name
        self.strength = Statistic("Strength", description="Strength is a measure of physical power.")
        self.intelligence = Statistic("Intelligence", description="Intelligence is a measure of cognitive ability.")
        # Add more stats as needed

    def __str__(self):
        return f"Character: {self.name}, Strength: {self.strength}, Intelligence: {self.intelligence}"

    def get_stats(self):
        return [self.strength, self.intelligence]  # Extend this list if there are more stats

# Create a Fireboy character
fireboy = Character(name="Fireboy")

# Print character information and stats
print(fireboy)
for stat in fireboy.get_stats():
    print(stat)
