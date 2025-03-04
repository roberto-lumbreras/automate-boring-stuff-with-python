import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count  = {}
for c in message:
    count.setdefault(c,0)
    count[c] = count[c]+1
pprint.pprint(count) # same as print(pprint.pformat(count))