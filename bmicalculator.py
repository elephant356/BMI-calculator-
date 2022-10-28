height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))



BMI = (weight / (height * height))
roundBMI = round(BMI, 2)

if roundBMI < 18.5:
  print(f"Your BMI is {roundBMI}. You are underweight")
elif roundBMI < 25:
  print(f"Your BMI is {roundBMI}. You weight is normal")
elif roundBMI < 30:
  print(f"Your BMI is {roundBMI}. You are overweight")
elif roundBMI < 35:
  print(f"Your BMI is {roundBMI}. You are obease")
else:
  print(f"Your BMI is {roundBMI}. PUT DOWN THE FORK!!!!")
