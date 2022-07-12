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