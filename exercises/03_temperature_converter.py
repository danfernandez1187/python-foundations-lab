temperature = float(input("Enter the temperature: "))
unit = input("Is this Celsius or Fahrenheit? Type C or F: ")

unit = unit.upper()

if unit == "C":
  converted_temperature = (temperature * 9 / 5) + 32
  print(f"{temperature:.1f} C is {converted_temperature:.1f} F")
elif unit == "F":
  converted_temperature = (temperature - 32) * 5 / 9
  print(f"{temperature:.1f} F is {converted_temperature:.1f} C")
else:
  print("Please enter C or F.")

