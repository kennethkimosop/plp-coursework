class Car:
  def move(self):
    return "Car is driving"
class Plane:
  def move(self):
    return "Plane is Flying"
class Boat:
  def move(self):
    return "Boat is Sailing"
class Person:
  def move(self):
    return "Person is walking"

# Polymorphism in action

if __name__ == "__main__":
  movers = [Car(), Plane(), Boat(),Person()]

  for mover in movers:
    print(mover.move())