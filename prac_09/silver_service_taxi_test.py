from silver_service_taxi import SilverServiceTaxi

# Create a new SilverServiceTaxi object
my_silver_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)

# Drive the SilverServiceTaxi 18 km
my_silver_taxi.drive(18)

# Print the SilverServiceTaxi's details and the current fare
print(my_silver_taxi)
print(f"Current fare: ${my_silver_taxi.get_fare():.2f}")

# for testing
assert my_silver_taxi.get_fare() == 48.8, f"Expected fare to be $48.80 but got {my_silver_taxi.get_fare():.2f}"

# Additional test for different fanciness
another_silver_taxi = SilverServiceTaxi("Luxury Taxi", 200, 3)
another_silver_taxi.drive(10)
print(another_silver_taxi)
print(f"Current fare: ${another_silver_taxi.get_fare():.2f}")

# for the new test
expected_fare = round(3 * 1.23 * 10 + 4.50, 1)
assert another_silver_taxi.get_fare() == expected_fare, f"Expected fare to be ${expected_fare:.2f} but got {another_silver_taxi.get_fare():.2f}"