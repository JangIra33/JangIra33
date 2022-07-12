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