# define the Vehicle class
class Car:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
carA = Car()
carA.name = "Ford"
carA.color = "Black"
carA.kind = "Sedan"
carA.value = 50000
print(carA.description())

carB = Car()
carB.name = "Jeep"
carB.color = "Red"
carB.kind = "Truck"
carB.value = 10000
print(carB.description())