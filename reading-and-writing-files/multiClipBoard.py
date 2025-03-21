import shelve,sys,pyperclip

savedContent = shelve.open('multiClipBoard')
if sys.argv[1] == 'delete'.lower() and len(sys.argv) == 3:
    del savedContent[sys.argv[2]]
elif sys.argv[1] == 'delete'.lower() and len(sys.argv) == 2:
    savedContent.clear()
elif sys.argv[1] == 'save'.lower() and len(sys.argv) == 3:
    savedContent[sys.argv[2]] = pyperclip.paste()
elif sys.argv[1] == 'list'.lower() and len(sys.argv) == 2:
    print(str(list(savedContent.keys())))
elif len(sys.argv) == 2:
    pyperclip.copy(savedContent[sys.argv[1]])
else:
    print('Available commands:\nlist\nsave [keyword]\n[keyword]')
savedContent.close()
