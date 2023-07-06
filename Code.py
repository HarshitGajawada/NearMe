import json

print("Welcome to the NearBy App.\n\n")
print("Where do you want to visit?\n")
print("1 - Theatres\n2 - Hospitals\n3 - Eateries\n4 - Petrol Stations\n5 - Banks")
place=input("Press the corresponding number(1-5): ")
check=99
while check==99:
    if place.isdigit():
        place=int(place)
        if 1<=place<=5:
            check=0
        else:
            place=input("enter valid input(1-5)")
            check=99  
    else:
        place=input("enter valid input(1-5)")
        check=99
    
# if  place.isdigit():
#     place=int(place)
#     while not 1 <= place <= 5 :
#         place = int(input("enter valid number(1-5): "))
# else:   
#     print("enter valid number(1-5):") 

json_files = ['theatres.json','hospitals.json','eateries.json','petrolstations.json','banks.json']


# if place==1:
#     with open('theatres.json','r') as theatres:
#         t = json.load(theatres)
#     for i in t["theatres"]:
#         print(i,"is",t["theatres"][i],"km away from you.\n")

def places(place,json_files):
    with open(json_files[place-1],'r') as file_name:
        d = json.load(file_name)
    for keys in d:
        for nkeys in d[keys]:
            print(nkeys,"is",d[keys][nkeys],"km away from you.\n")
places(place,json_files)





        
        
    
    

    
