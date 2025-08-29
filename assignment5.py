class Car:
    def __init__(self, brand, model, year):
        # Encapsulated attributes
        self._brand = brand
        self._model = model
        self._year = year
        self._mileage = 0  # protected attribute

    def drive(self, miles):
        """Simulate driving, increasing mileage."""
        if miles > 0:
            self._mileage += miles
            print(f"{self._brand} {self._model} drove {miles} miles.")
        else:
            print("Miles must be a positive number.")

    def get_details(self):
        """Return a formatted string with car details."""
        return f"{self._year} {self._brand} {self._model}"

    def max_speed(self):
        """Generic max speed—overridden in subclasses."""
        return "Max speed: 100 mph"

    def get_mileage(self):
        """Accessor for mileage (demonstrating encapsulation)."""
        return self._mileage


class Audi(Car):
    def __init__(self, model, year, quattro=False):
        super().__init__("Audi", model, year)
        self._quattro = quattro  # specific feature
        self._max_speed = 155 if quattro else 140

    def max_speed(self):
        """Override: show different max speed if quattro."""
        return f"Max speed: {self._max_speed} mph (quattro: {self._quattro})"

    def toggle_quattro(self):
        """Enable or disable quattro system."""
        self._quattro = not self._quattro
        self._max_speed = 155 if self._quattro else 140
        print(f"Quattro toggled to {self._quattro}.")


# Usage demonstration
if __name__ == "__main__":
    generic = Car("Generic", "Model X", 2020)
    audi_a4 = Audi("A4", 2023)
    audi_rs = Audi("RS", 2024, quattro=True)

    print(generic.get_details())        # Base class behavior
    print(audi_a4.get_details())        # Inherited method
    print(audi_rs.get_details())

    print(generic.max_speed())          # Car version
    print(audi_a4.max_speed())          # Overridden (quattro off)
    print(audi_rs.max_speed())          # Overridden (quattro on)

    audi_a4.drive(50)
    print("Mileage:", audi_a4.get_mileage())

    audi_a4.toggle_quattro()
    print(audi_a4.max_speed())
