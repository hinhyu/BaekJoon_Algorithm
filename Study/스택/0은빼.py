n= int(input())
list=[]

for i in range(n):
    a = int(input())
    list.append(a)
    if a == 0:
        list.pop()
        list.remove(list[-1])
result=sum(list)
print(result)