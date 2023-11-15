def fatorial(num):
    if num<0: return 0
    fat = 1
    for i in range(1, num+1):
        fat *= i
    return(fat)

print(fatorial(5))

# def hello(name):
#     return f'hello, {name}'  

