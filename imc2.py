from os import system

system('cls')

weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))
result = weight / (height ** 2)

if result < 17:
    print(f"Your IMC is {result:.2f}. Your level is very underweight.")
elif 17 <= result <= 18.49:
    print(f"Your IMC is {result:.2f}. Your level is underweight.")
elif 18.5 <= result <= 24.99:
    print(f"Your IMC is {result:.2f}. Your level is normal weight.")
elif 25 <= result <= 29.99:
    print(f"Your IMC is {result:.2f}. Your level is overweight.")
elif 30 <= result <= 34.99:
    print(f"Your IMC is {result:.2f}. Your level is obesity grade 1.")
elif 35 <= result <= 39.99:
    print(f"Your IMC is {result:.2f}. Your level is obesity grade 2 (severe).")
else:
    print(f"Your IMC is {result:.2f}. Your level is obesity grade 3 (morbid).")
