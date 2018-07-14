def duplicates1(a):
    result = []
    for i in a:
        if i not in result:
            result.append(i)
    return sorted(result)

def duplicates2(a):
    return sorted(list (set(a)))
