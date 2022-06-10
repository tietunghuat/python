#Q1
#================================================
import random
nice = list(range(1, 26))
random.shuffle(nice)
for i in range(5):
    for j in range(5):
        if nice[i*5+j] != '##' and nice[i*5+j] < 10:
            print('0'+str(nice[i*5+j]), end='  ')
        else:
            print(str(nice[i*5+j]), end='  ')
    print()
print()
while True:
    input_num = int(input('input a number(0 to quit):'))
    if input_num ==0:
        break
    else:
        for i in range(5):
            for j in range(5):
                if nice[i*5+j] == input_num:
                    nice[i*5+j] = '##'
                if nice[i*5+j] != '##' and nice[i*5+j] <10:
                    print('0'+str(nice[i*5+j]), end='  ')
                else:
                    print(str(nice[i*5+j]), end='  ')
            print()
        print()
#========================================================


#Q2
#==========================================================
import string
def pypart2(n):
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
n = 6
pypart2(n)

a=5
for i in range(a):
    for j in range(a):
        if i==(a-1) or j==(a-1) or i+j==(a-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
#=====================================================



#Q3
#BOYSNAME=NAMES.TXT--------------------------------
with open('BoyNames.txt', 'r') as file1:
    with open('names.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('new.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

infile = open("new.txt", "r")
namelist = []
for line in infile:
    namelist.append(line.rstrip())

print("BoyNames.txt = names.txt",namelist)
#-----------------------------------------------------


#GirlSNAME=NAMES.TXT--------------------------------
with open('GirlNames.txt', 'r') as file1:
    with open('names.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('new.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

file = open("new.txt", "r")
list = []
for line in file:
    list.append(line.rstrip())

print("GirlNames.txt = names.txt", list)
#----------------------------------------------------