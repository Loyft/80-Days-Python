print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?\n"))
tip_percentage = float(input("What percentage tip would you like to give?\n"))
amount_people = float(input("How many people to split the bill?\n"))

tip_value = 1 + (tip_percentage / 100)
tip_per_person = round((total_bill * tip_value) / amount_people, 2)

# Formatting for cases with less than 2 digits after .
tip_per_person = "{:.2f}".format(tip_per_person)

print(f"Each person should pay: {tip_per_person}")
