def calculate_discount(price,discount_percent):
  discount = 0.2 * price
  if discount_percent >= 20:
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price
  else:
    return price # no discount if less than 20 percent
  
original_price = float(input("ENter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))


final_price = calculate_discount(original_price, discount_percent)
if discount_percent >= 20:
  print(f"Final price after {discount_percent} % disocunt is: {final_price}")
else:
  print(f"No discount applied. Original price: {final_price}")
