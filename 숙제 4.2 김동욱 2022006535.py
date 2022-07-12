#재귀 함수
#def sigma_product_power_of_2(n):
#    if n>0:
#        return sigma_product_power_of_2(n-1) + n*(2**(n-1))
#    else:
#        return 0

#꼬리 재귀 함수
#def sigma_product_power_of_2(n):
#    def loop(n,total):
#        if n>0:
#            total += n*(2**(n-1))
#            return loop(n-1,total)
#        elif n==0:
#            return total
#        else:
#            return 0
#    return loop(n,0)

#while문
#def sigma_product_power_of_2(n):
#    total = 0
#    while n!=0:
#        total += n*(2**(n-1))
#        n=n-1
#    return total

#def sigma_product_power_of_2(n):
#    return (n-1) * 2**n + 1
#이 함수n에 1을 넣으면 1이 나오므로 이 함수는 n=1일 때 성립한다 이 함수가 자연수 n일 때 성립한다고 가정하면
#(n-1) * 2**n +1 = n*(2**(n-1)) +n-1*(2**(n-2))......+1*(2**(1-1))이 성립합니다. 이때 양변에 2를 곱하고 2**(n+1)을 더한 후
#1을 빼주면 n*2**(n+!) +1 = (n+1)*(2**n)+n*(2**(n-1)).....+1*(2**(1-1))이므로 이 식은 n+1일때 성립합니다. 따라서 수학적 귀납법에 의하여
#이 식은 자연수 n에 대하여 항상 성립합니다.


# Test code
#print(sigma_product_power_of_2(0)) # 0
#print(sigma_product_power_of_2(1)) # 1
#print(sigma_product_power_of_2(2)) # 5
#print(sigma_product_power_of_2(3)) # 17
#print(sigma_product_power_of_2(4)) # 49
#print(sigma_product_power_of_2(5)) # 129
#print(sigma_product_power_of_2(6)) # 321
#print(sigma_product_power_of_2(7)) # 769