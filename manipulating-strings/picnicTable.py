def printPicnic (picnicDict, leftWidth, righWidth):
    print('PICNIC ITEMS'.center(leftWidth+righWidth,'-'))
    for k,v in picnicDict:
        print(str(k).ljust(leftWidth,'.')+str(v).rjust(righWidth))
picnic = {'sandwiches': '4', 'apples': '12', 'cups': '2', 'cookies': '8000'}
printPicnic(picnic.items(),12,24)