import random

'''
i = 0
num = int(input('Enter a number: '))
while sum != num:
    a = (random.randint(0,100))
    b = (random.randint(0,100))
    c = (random.randint(0, 100))
    d = (random.randint(0,100))
    sum = a + b + c + d
    #print(a,b)

    if sum / num == 1:
        break
    else:
        pass
    i += 1
print(a,b,c,d)
#print(sum)
'''
print('Enter a number and I will print out Four \nRandom numbers that will sum up to your number')

def list():
    a = 0
    while a <= 3:
        my_list.append(random.randint(0,100))
        a += 1
num1 = int(input('Enter a number: '))
i = 0
list_sum = 0

while list_sum != num1:
    my_list = []
    list()
    list_sum = sum(my_list)

    if list_sum == num1:
        break
    else:
        pass
    i += 1
print('The random numbers are = {}'.format(my_list))
print(f'The sum of the numbers is {list_sum}')
