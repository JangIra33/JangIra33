#숙제 5-1

#재귀 함수

def remove_one(x,xs):
    if xs != []:
        if x == xs[0]:
            return xs[1:]
        else:
            return [xs[0]] + remove_one(x,xs[1:])
    else:
        return xs

#꼬리 재귀 함수

def remove_one(x,xs):
    def loop(xs,left):
        if xs != []:
            if x == xs[0]:
                left = left + xs[1:]
                return left
            else:
                left += [xs[0]]
                return loop(xs[1:],left)
        else:
            return left
    return loop(xs,[])
#while문

def remove_one(x,xs):
    left = []
    while xs != []:
        if x == xs[0]:
            left = left + xs[1:]
            return left
        else:
            left.append(xs[0])
            xs = xs[1:]
    return left

# Test code
print(remove_one(3,[]))        # []
print(remove_one(3,[3]))       # []
print(remove_one(3,[2]))       # [2]
print(remove_one(3,[2,3,2,3])) # [2, 2, 3]
print(remove_one(3,[2,2,2,3])) # [2, 2, 2]
print(remove_one(3,[2,2,2,2])) # [2, 2, 2, 2]

#문제 5-2
#재귀함수

def remove_all(x,xs):
    if xs != []:
        if x == xs[0]:
            return remove_all(x,xs[1:])
        else:
            return [xs[0]] + remove_all(x,xs[1:])
    else:
        return xs

#꼬리 재귀함수

def remove_all(x,xs):
    def loop(xs,left):
        if xs != []:
            if x == xs[0]:
                return loop(xs[1:],left)
            else:
                left += [xs[0]]
                return loop(xs[1:],left)
        else:
            return left
    return loop(xs,[])

#while문

def remove_all(x,xs):
    left = []
    while xs != []:
        if x == xs[0]:
            xs = xs[1:]
        else:
            left += [xs[0]]
            xs = xs[1:]
    return left

# Test code
print(remove_all(3,[]))        # []
print(remove_all(3,[3]))       # []
print(remove_all(3,[3,3,3,3])) # []
print(remove_all(3,[2]))       # [2]
print(remove_all(3,[2,3,2,3])) # [2, 2]
print(remove_all(3,[2,2,2,3])) # [2, 2, 2]
print(remove_all(3,[2,2,2,2])) # [2, 2, 2, 2]

#숙제 5.3 시간 없어서 못했습니다.

def remove_duplicates(xs):
    if len(xs) >= 2:
        head = xs[0]
        if head not in xs[1:]:
            return [head] + remove_duplicates(xs[1:])
        else:
            xs.remove(head)
            return [head] + remove_duplicates(xs[1:])           
    else:
        if [head] == xs:
            return []
        else:
            return xs

# Test code    
print(remove_duplicates([]))                  # []
print(remove_duplicates([1]))                 # [1]
print(remove_duplicates([1,1]))               # [1]
print(remove_duplicates([1,1,1,1]))           # [1]
print(remove_duplicates([4,2,3,2,2,4,3,2,1])) # [4, 2, 3, 1]

#숙제 5-4
#재귀함수

def union(xs,ys) :
    if xs != []:
        if xs[0] not in ys:
            return [xs[0]] + union(xs[1:],ys)
        else:
            return union(xs[1:],ys)
    else:
        return ys

#꼬리 재귀 함수

def union(xs,ys) :
    def loop(xs,zs):
        if xs != []:
            if xs[0] not in ys:
                zs.append(xs[0])
            return loop(xs[1:],zs)
        else:
            return zs + ys
    return loop(xs,[])

#while문

def union(xs,ys) :
    zs = []
    while xs != []:
        if xs[0] not in ys:
            zs.append(xs[0])
        xs = xs[1:]
    return zs + ys

#for문

def union(xs,ys) :
    zs = []
    for x in xs:
        if x not in ys:
            zs.append(x)
    return zs + ys

# Test code    
print(union([],[]))           # []
print(union([1,2],[]))        # [1, 2]
print(union([],[3,4]))        # [3, 4]
print(union([1,2],[3,4]))     # [1, 2, 3, 4]
print(union([1,2],[2,3]))     # [1, 2, 3]
print(union([1,2],[2,1]))     # [2, 1]
print(union([1,2,3],[3,2,1])) # [3, 2, 1]
print(union([1,2,3],[3,2,4])) # [1, 3, 2, 4]
print(union([1,2,3],[4,5,6])) # [1, 2, 3, 4, 5, 6]

#숙제 5-5
#재귀 함수

def intersection(xs,ys):
    if xs != []:
        if xs[0] in ys:
            return [xs[0]] + intersection(xs[1:],ys)
        else:
            return intersection(xs[1:],ys)
    else:
        return xs

#꼬리 재귀 함수

def intersection(xs,ys):
    def loop(xs,zs):
        if xs != []:
            if xs[0] in ys:
                zs += [xs[0]]
                return loop(xs[1:],zs)
            else:
                return loop(xs[1:],zs)
        else:
            return zs
    return loop(xs,[])

#while문

def intersection(xs,ys):
    zs = []
    while xs != []:
        if xs[0] in ys:
            zs = zs + [xs[0]]
            xs = xs[1:]
        else:
            xs = xs[1:]
    return zs

#for문

def intersection(xs,ys):
    zs = []
    for x in xs:
        if x in ys:
            zs.append(x)
    return zs

# Test code    
print(intersection([],[]))           # []
print(intersection([1,2],[]))        # []
print(intersection([],[3,4]))        # []
print(intersection([1,2],[3,4]))     # []
print(intersection([1,2],[2,3]))     # [2]
print(intersection([1,2],[2,1]))     # [1, 2]
print(intersection([1,2,3],[3,2,1])) # [1, 2, 3]
print(intersection([1,2,3],[3,2,4])) # [2, 3]
print(intersection([1,2,3],[4,5,6])) # []

#숙제 5-6
#재귀 함수

def difference(xs,ys) :
    if xs != []:
        if xs[0] in ys:
            return difference(xs[1:],ys)
        else:
            return [xs[0]] + difference(xs[1:],ys)
    else :
        return []

#꼬리 재귀 함수

def difference(xs,ys) :
    def loop(xs,zs):
        if xs != []:
            if xs[0] not in ys:
                zs.append(xs[0])
            return loop(xs[1:],zs)
        else:
            return zs
    return loop(xs,[])

#while문

def difference(xs,ys) :
    zs = []
    while xs != []:
        if xs[0] not in ys:
            zs.append(xs[0])
        xs = xs[1:]
    return zs

#for문

def difference(xs,ys) :
    zs = []
    for x in xs:
        if x not in ys:
            zs.append(x)
    return zs


# Test code    
print(difference([],[]))           # []
print(difference([1,2],[]))        # [1, 2]
print(difference([],[3,4]))        # []
print(difference([1,2],[3,4]))     # [1, 2]
print(difference([1,2],[2,3]))     # [1]
print(difference([1,2],[2,1]))     # []
print(difference([1,2,3],[3,2,1])) # []
print(difference([1,2,3],[3,2,4])) # [1]
print(difference([1,2,3],[4,5,6])) # [1, 2, 3]