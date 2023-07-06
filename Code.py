import json

print("Welcome to the NearBy App.\n\n")
print("Where do you want to visit?\n")
print("1 - Theatres\n2 - Hospitals\n3 - Eateries\n4 - Petrol Stations\n5 - Banks")
place=int(input("Press the corresponding number(1-5): "))

if not 1 <= place <= 5:
    while not 1 <= place <= 5:
        place = int(input("enter valid number(1-5): "))


if place==1:
    with open('theatres.json','r') as theatres:
        t = json.load(theatres)
    for i in t["theatres"]:
        print(i,"is",t["theatres"][i],"km away from you.\n")

        
        
    
    

    
