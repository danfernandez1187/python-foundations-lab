def create_greeting(name, city):
  return f"Hello, {name}! I heard you're building Python skills from {city}."

user_name = input("What is your name? ")
user_city = input("What city are you in? ")

greeting = create_greeting(user_name, user_city)

print(greeting)
