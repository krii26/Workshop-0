temperatures = [1,3,5,7,9,11,13,15,17,19,21]

temperatures_fahrenheit = []

for temp in temperatures:
    fahrenheit = (temp * 9/5) + 32
    temperatures_fahrenheit.append(fahrenheit)

print("Temperatures in Fahrenheit is:", temperatures_fahrenheit)
