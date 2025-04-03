# Base Class: Vehicle
class Vehicle:
    def move(self):
        """Default move behavior for all vehicles."""
        print("The vehicle is moving.")

# Derived Class: Car
class Car(Vehicle):
    def move(self):
        """Override move method for Car."""
        print("Driving 🚗")

# Derived Class: Plane
class Plane(Vehicle):
    def move(self):
        """Override move method for Plane."""
        print("Flying ✈️")

# Derived Class: Boat
class Boat(Vehicle):
    def move(self):
        """Override move method for Boat."""
        print("Sailing 🚤")

# Create objects of the classes
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism by calling the same method on different objects
vehicles = [car, plane, boat]
for vehicle in vehicles:
    vehicle.move()
