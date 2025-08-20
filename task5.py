
fact=1
def factorial(num):
    global fact
    if num<2:
        print(num)
    else:
        for i in range(2, num+1):
            fact = fact * i
    return fact

num=int(input('Enter a number:'))
result=factorial(num)
print('factorial of',num,'is',result)


