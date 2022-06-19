# names=["mansi"]
name=input("please enter the string ")
name_lower = name.lower()
print(name + "\n")
print(name_lower + "\n")
name_find=name_lower.find("mansi")
print(name_find)

if (name_find==0):
    print("yes is talk about mansi")
else:
    print("no is not talk about mansi")