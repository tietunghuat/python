infile = open("BoyNames.txt","r")
namelist = []
for line in infile:
    print(line)
    namelist.append(line.rstrip())

print(namelist)
target=input("enter a boy's name:")

if target in namelist:
    print("found it !")
else:
    print("not in the list")

b="Christopher"
a=len(b)
print(a)


# for name in namelist:
#     if name.startswith("B"):
#         print(name)


# name = []
# infile = open("BoyNames.txt", "r")
# import string
# di={}.fromkeys(string.ascii_letters,0)
# for name in infile:
#     di[name[0]]+=1
# print(di)
