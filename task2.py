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

mild_count = len(mild)
print(f"Times for mild was {mild_count}")

comfortable_count = len(comfortable)
print(f"Times for comfortable was: {comfortable_count}")

cold_count = len(cold)
print(f"Times for cold was: {cold_count}")
