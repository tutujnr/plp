# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_level):
        # Constructor to initialize attributes
        self.brand = brand
        self.model = model
       # Encapsulated attribute
        self._battery_level = battery_level 
        self.is_on = False

    def turn_on(self):
        """Turn on the smartphone."""
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def turn_off(self):
        """Turn off the smartphone."""
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def check_battery(self):
        """Check the current battery level."""
        print(f"{self.brand} {self.model} battery level: {self._battery_level}%")

# Derived Class: SmartphoneWithCamera
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_level, camera_megapixels):
        # Inheritance from Smartphone
        super().__init__(brand, model, battery_level)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        """Simulate taking a photo."""
        print(f"Taking a {self.camera_megapixels} MP photo with the {self.brand} {self.model}.")

# Create objects of the classes
basic_phone = Smartphone("Samsung", "Galaxy S21", 80)
smartphone_with_camera = SmartphoneWithCamera("Apple", "iPhone 13", 90, 12)

# Test the methods
basic_phone.turn_on()
basic_phone.check_battery()

smartphone_with_camera.turn_on()
smartphone_with_camera.take_photo()
smartphone_with_camera.check_battery()
