contacts = []

for number in range (1, 3):
  print(f"Contact {number}")

  name = input("Name: ")
  phone = input("Phone: ")
  email = input("Email: ")

  contact = {
      "name": name,
      "phone": phone,
      "email": email
  }

  contacts.append(contact)

print("Contact book:")

for contact in contacts:
  print(f"{contact['name']} | {contact['phone']} | {contact['email' ]}")
