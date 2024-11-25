# Example list of temperatures for each hour of the day (24 hours)
temperatures = [2, 12, 8, 15, 19, 21, 5, 13, 18, 9, 14, 11, 16, 17, 20, 22, 25, 26, 27, 23, 21, 19, 18, 16]

# Step 1: Create empty lists for night, evening, and day temperatures
night = []
evening = []
day = []

# Step 2: Classify the temperatures based on time of day
for i, temp in enumerate(temperatures):
    if 0 <= i <= 7:  # Night (00:00-08:00)
        night.append(temp)
    elif 8 <= i <= 15:  # Evening (08:00-16:00)
        evening.append(temp)
    elif 16 <= i <= 23:  # Day (16:00-24:00)
        day.append(temp)

# Step 3: Calculate the average day-time temperature
average_day_temp = sum(day) / len(day) if day else 0  # Check to avoid division by zero

# Step 4: Print the results
print("Night temperatures (00:00 - 08:00):", night)
print("Evening temperatures (08:00 - 16:00):", evening)
print("Day temperatures (16:00 - 24:00):", day)
print(f"Average day-time temperature (16:00 - 24:00): {average_day_temp:.2f}°C")
