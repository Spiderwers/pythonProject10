import itertools
alphabet = "УЧЕНИК"
ar = itertools.product(alphabet, repeat = 5)
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    if e[0] == 'у' and e[-1] == 'К':
        count += 1
print(count)


import itertools
alphabet = "ГОД"
con = 'ГД'
ar = itertools.product(alphabet, repeat = 5)
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    if e[0] in con:
        count += 1
print(count)
