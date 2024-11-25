cold = []
mild = []
comfortable = []

temperatures = [1,3,5,7,9,11,13,15,17,19,21]

for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp <= 15:
        mild.append(temp)
    elif 15 < temp <= 20:
        comfortable.append(temp)

print("Cold temperatures (below 10°C):", cold)
print("Mild temperatures (between 10°C and 15°C):", mild)
print("Comfortable temperatures (between 15°C and 20°C):", comfortable)
