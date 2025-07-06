for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

succesful = False

for number in range(3):
    print("Attempt")
    if succesful:
        print("Succesful")
        break
else:
    print("Attempted 3 times and failed!")
