name = input("Enter your name: ")
city = input("Enter your city: ")
age = input("Enter your age: ")
age_int = int(age)
dream = input("What is your dream? ")
print(
    f"--- PROFILE CARD ---\nName: {name}\nCity: {city}\nAge: {age_int}\nDream: {dream}\nIn 10 years you will be {age_int + 10}"
)
