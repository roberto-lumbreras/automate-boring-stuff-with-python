import sys, time

indentIncreasing = True
indent = 0
try:
    while True:
        print(' ' * indent, end = '')
        print('********')
        time.sleep(0.1)
        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent = indent-1
            if not indent:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()