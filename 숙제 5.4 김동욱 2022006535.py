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