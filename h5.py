import random

x = 1
while x <= 10:
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    if n1 < n2:
        n1, n2 = n2, n1
    ans = n1 - n2
    ansu = eval(input('what is {:d} - {:d}: '.format(n1, n2)))
    if ans == ansu:
        print('huzzah correct')
    else:
        print('dead wrong')
x += 1

print('all done')