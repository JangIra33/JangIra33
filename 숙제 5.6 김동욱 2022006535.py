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