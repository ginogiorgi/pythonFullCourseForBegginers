temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink Water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

print(f"It's {"Warm" if temperature >= 25 else "Cold"}")
