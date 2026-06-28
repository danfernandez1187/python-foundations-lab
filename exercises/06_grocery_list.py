groceries = []

item_one = input("Enter your first grocery item: ")
item_two = input("Enter uyour second grocery item: ")
item_three = input("Enter your third grocery item: ")

groceries.append(item_one)
groceries.append(item_two)
groceries.append(item_three)

print("Your grocery list:")

for item in groceries:
  print(f"- {item}")
