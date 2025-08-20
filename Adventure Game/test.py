weight = float(input("weight"))
unit = input("(k)g or (L)bs")

if unit.lower() == "l":
   print(weight * 0.45)
elif unit.lower() == "k":
   print(weight * 2.2)
else:
   print("Please enter a valid unit (k or L).")
    


