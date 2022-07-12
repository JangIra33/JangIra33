def find_anagrams(List):
    memo = [[0 for _ in range(10)] for i in range(len(List))]
    for i in range(len(List)):
        for j in range(4):
            memo[i][int(List[i][j])] += 1
    for i in range(len(List)):
        P = List[i]
        for j in range(1,len(List)):
            if memo[i] == memo[j]:
                if List[i] != List[j]:
                    if List[j] not in P:    
                        P+= " "+List[j]
                    memo[j] = j
                else:
                    pass
        if P != List[i]:
            print(P)
    

find_anagrams(["0952", "5239", "1270", "8581", "7458", "3414", "7906", "2356", "4360", "3491", 
 "6232", "5927", "2735", "2509", "5849", "8457", "9340", "1858", "8602", "5784"])