def unique_in_order(iterable):
    if iterable.isempty(): return ""
    x = [iterable[0]]
    [x.append(iterable[i]) for i in range(1,len(iterable)) if x[len(x)-1] != iterable[i]]
    return x