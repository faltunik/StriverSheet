def maximumValue(items, n, w):
    # we will assume items is 2d matrix, with a[0] = value
    # so maybe items = [[w], [v]]
    #print('itmes is ', items)
    items = [[i[1]/i[0], i[0]] for i in items]
    items.sort(reverse=True)
    #print(items)
    v = 0
    for i in items:
        if w ==0:
            break
        v += i[0]*(min(i[1], w))
        w = w- min(i[1], w)
    return v