textOne = input()
textTwo = input()

textOne = list(textOne)
textTwo = list(textTwo)

setOne = {x for x in textOne}
setTwo = {x for x in textTwo}

y = setOne.intersection(setTwo)

for item in y:
    print(item)












