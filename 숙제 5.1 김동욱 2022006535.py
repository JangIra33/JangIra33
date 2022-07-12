#숙제 5-1

#재귀 함수

def remove_one(x,xs):
    if xs != []:
        if x == xs[0]:
            return xs[1:]
        else:
            return [xs[0]] + remove_one(x,xs[1:])
    else:
        return []

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

