from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel, 1.23)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string representation like a Taxi but with flagfall added."""
        return f"{super().__str__()} plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip including the flagfall."""
        fare = super().get_fare() + SilverServiceTaxi.flagfall
        return round(fare, 1)  # round to nearest 10 cents