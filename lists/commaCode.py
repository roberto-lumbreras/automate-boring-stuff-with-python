def listToString(list):
    string = ''
    for x in range(len(list)):
        if x == len(list)-1 and x != 0:
            string+=' and '+list[x]
        elif x!=0:
            string += ', '+list[x]
        else:
            string+=list[x]
    return string
list = ['cat','mouse','dog']
list2 = []
list3 = ['cat']
list4 = ['cat','dog']
print(listToString(list))
print(listToString(list2))
print(listToString(list3))
print(listToString(list4))