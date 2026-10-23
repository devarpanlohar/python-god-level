print("My name is Arpan.")
print("My city is Tamluk.")
print("I want to build myself python monster with python.")

name = "Arpan"
age = 25
city = "Tamluk"

# Put f before the quote, and variables inside {}
print(f"My name is {name} and I am {age} years old from {city}.")
print(f"In 5 years, I will be {age + 5}")

name = input("Enter your name: ")
age = input("Enter your age: ")
# age is text right now, so we convert it
age_num = int(age)  # str -> int

print(f"Hello {name}, next year you will be {age_num + 1}")
