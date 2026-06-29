try:
  age = int(input("Enter your age: "))
  next_year_age = age + 1
  print(f"Next year you will be {next_year_age}.")
except ValueError:
  print("Please enter a whole numner, like 25.")
