#어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 
# 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
#자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
# 216(분해합)입력 => 198(생성자) + 1 + 9 + 8

N = int(input())
print_num = 0
for i in range(1, N+1):
     div_num = list(map(int, str(i)))    #1~n까자의 값을 문자열로 리스트에 저장 [1]~[2,1,6] 형태로 저장됨
     sum_num = i + sum(div_num)          #216의 분해합은 198(=198+1+9+8)인데 198번째 리스트인 [1,9,8] 를 꺼내와서 몇 번째 숫자(i) + 리스트를 더한 값 
     if(sum_num == N):                   #위에서 더한 값이 n이면
         print_num = i                   #그게 몇 번째 수(최소생성자)가 된다.
         break
print(print_num)