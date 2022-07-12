def identical(x,y,z):
    if x==y==z:
        return "triple"
    elif x==y!=z or y==z!=x or z==x!=y:
        return "twin"
    else:
        return None 

# Test code
print(identical(2,3,4)) # None
print(identical(2,2,4)) # (2, "twin")
print(identical(2,3,2)) # (2, "twin")
print(identical(2,3,3)) # (3, "twin")
print(identical(3,3,3)) # (3, "triple")