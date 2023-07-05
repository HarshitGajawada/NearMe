print()
print("Welcome to the NearBy App.")
print()
print("1) Movies\n2) Hospital\n3) Eateries\n4) Petrol Station\n5) Banks")
places=["Movies","Hospital", "Eateries", "Petrol Station", "Banks"]
place=input("Where do you want to visit? ")
while place not in places:
    print("Please choose places from the options only.")
    place=input("Where do you want to visit? ")

print("Hello Github.")