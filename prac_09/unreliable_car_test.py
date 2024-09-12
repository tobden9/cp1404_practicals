from unreliable_car import UnreliableCar

# Create a new unreliable car object
my_unreliable_car = UnreliableCar("Old Car", 100, 50)

# Attempt to drive the car 40 km
distance_driven = my_unreliable_car.drive(30)
print(f"Attempted to drive 40 km, actually drove {distance_driven} km")

# Attempt to drive the car 100 km
distance_driven = my_unreliable_car.drive(100)
print(f"Attempted to drive 100 km, actually drove {distance_driven} km")