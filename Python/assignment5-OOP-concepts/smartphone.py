class Smartphone:
    def __init__(self,brand,model,storage,battery):
      # attributes
      self.brand = brand
      self.model = model
      self.storage = storage
      self.battery = battery

    # method to show smartphone details
    def display_info(self):
      return f"{self.brand} {self.model} with {self.storage}GB and {self.battery}mAh battery."
    
    # method to simulate using the phone
    def use_phone(self,hours):
      self.battery -= hours *100
      return f"Used {self.model} for {hours} hours. Battery now at {self.battery}mAh."
    
    # method to charge the phone
    def charge(self,amount):
      self.battery  += amount
      return f"Charged {self.model}. Battry now at {self.battery}mAh."


# Example usage
if __name__ == "__main__":
  phone1 = Smartphone("Samsung", "S23", 256, 5000)
  phone2 = Smartphone("Apple", "iPhone 14", 128,3200)

  print(phone1.display_info())
  print(phone2.display_info())
  print(phone1.use_phone(2))
  print(phone2.charge(500))