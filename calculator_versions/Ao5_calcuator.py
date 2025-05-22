times = []


# Function to convert time in minutes:seconds.milliseconds to total seconds
def convert_to_seconds(time_str):
    if ":" in time_str:
        minutes, seconds = time_str.split(":")
        return float(minutes) * 60 + float(seconds)
    else:
        return float(time_str)


# Input 5 solves
for i in range(1, 6):
    time_str = input(f"Solve {i} (format mm:ss.ss): ")
    times.append(convert_to_seconds(time_str))

# Process times
times.sort()
times.pop(0)  # Remove the fastest solve
times.pop(-1)  # Remove the slowest solve

# Calculate average of middle 3 solves
average = sum(times) / 3

# Convert the average back to minutes:seconds.milliseconds format
minutes = int(average // 60)
seconds = average % 60
print(f"Ao5: {minutes}:{seconds:05.2f}")
