def printTable(table):
    colWidths = []
    maxColumnWidth = 0
    for column in table:
        for value in column:
            if len(value)>maxColumnWidth:
                maxColumnWidth = len(value)
        colWidths.append(maxColumnWidth)
        maxColumnWidth = 0
    for i in range(len(table[0])):
        for k in range(len(table)):
            print(str(table[k][i]).rjust(colWidths[k]), end = ' | ')
        print()
        
table = [['Iron man', 'Black panther', 'Scarlet Witch'],
         ['Wolverine', 'Magneto', 'Thor'],
         ['Spider-man', 'Venom', 'Doctor Strange']]
printTable(table)


            