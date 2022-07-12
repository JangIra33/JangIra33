#재귀 함수
#def sigma_power_of_2(n):
#    if n>=0:
#        return 2**n + sigma_power_of_2(n-1)
#    else:
#        return 0

#꼬리 재귀 함수
#def sigma_power_of_2(n):
#    def loop(n,total):
#        if n>0:
#            total += 2**n
#            return loop(n-1,total)
#        elif n==0:
#            total += 1
#            return total
#        else:
#            return 0
#    return loop(n,0)

#while 문
#def sigma_power_of_2(n):
#    total = 0
#    while n>=0:
#        total += 2**n
#        n=n-1
#    return total


#def sigma_power_of_2(n):
#    return 2**(n+1)-1
#이 함수에 0을 넣은 값은 1이 나오므로 이 함수는 n=0일 때 성립합니다. 그리고 이 함수의 변수가 n일 때 함수가 만족한다고 가정하면
#2**(n+1)-1 = 2**n+2**(n-1).....+2**0이 됩니다. 이때 양변에 2를 곱하고 1을 더하면 2**(n+2)-1 = 2**(n+1)+2**n+2**(n-1)....2**0이 됩니다.
#따라서 이 함수는 n+1일 때 성립하므로 이 함수는 모든 자연수 n에 대하여 성립한다고 볼 수 있습니다.



#Test code
#print(sigma_power_of_2(0)) # 1
#print(sigma_power_of_2(1)) # 3
#print(sigma_power_of_2(2)) # 7
#print(sigma_power_of_2(3)) # 15
#print(sigma_power_of_2(4)) # 31
#print(sigma_power_of_2(5)) # 63
#print(sigma_power_of_2(6)) # 127
#print(sigma_power_of_2(7)) # 255