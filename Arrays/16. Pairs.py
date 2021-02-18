# Question1 - Missing Number

items = [1,4,6,7,3,8,4,9,0,]

def pairsOfNumber(list, value):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == value:
                print(list[i],list[j])
   

pairsOfNumber(items, 9)

