
listOne = []
listTwo = []

for item in range(0, 25):
    if item % 3 == 0:
        listOne.append(item)
print(listOne)

for item in range(0, 25):
    if item % 5 == 0:
        listTwo.append(item)
print(listTwo)

setOne = {x for x in listOne}
setTwo = {x for x in listTwo}

res = setOne.intersection(setTwo)

print(res)
