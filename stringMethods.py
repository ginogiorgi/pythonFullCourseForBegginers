first = "Gino"
last = "Giorgi"
full = f"{first} {last}"
test = f"{len(first)} {2 + 2}"
test2 = "     Gino Giorgi"

print(full, test)
print(last.upper())
print(last.lower())
print(test2.strip())
print(test2.find("or"))
print(test2.find("Or"))
print(test2.replace("o", "i").strip())
print("o" in test2)
print("o" not in test2)
