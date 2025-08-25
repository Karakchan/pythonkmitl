weight = float(input("Enter your weight : "))
unit = input(" Kilograms or Pounds ?( K or P) : ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "P":
    weight = weight / 2.205
    unit = "Kg"
else:
    print(f"{weight} is an Invalid ")

print(f"You are {round(weight, 2)} {unit}")