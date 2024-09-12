class Band:
    """Band class to manage a list of musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band's list of musicians."""
        self.musicians.append(musician)

    def play(self):
        """Simulate the band playing by having each musician play their instrument."""
        for musician in self.musicians:
            print(musician.play())