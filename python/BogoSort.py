from random import shuffle

test = [2, 4, 6, 1, 5, 3]
recs = 1

def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False

    return True

def bogosort(l):
    global recs
    print('List state:', l, 'at', recs, 'recursions')

    if is_sorted(l):
        return l

    recs += 1
    shuffle(l)
    return bogosort(l)

bogosort(test)
print('for a list length of', len(test))
print('We did', recs, 'recursions')