bill_total = float(input("What was the bill total? "))
tip_percent = float(input("What tip percentage do you want to leave? "))

tip_amount = bill_total * (tip_percent / 100)
final_total = bill_total + tip_amount

print(f"Bill total: ${bill_total:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Final total: ${final_total:.2f}")
