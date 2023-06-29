import random
print('please choose a number')
typ = int(input('what do you want addition-1 or subtraction-2 = '))
addition = 1
subtraction = 2
times = int(input('Enter amounts of time you want to do the questions = '))
right = 0
if typ == addition:
    for x in range(times):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(a, '+', b, 'equals?')
        user = int(input())
        check = a + b
        if user == check:
            print('Correct ✔!')
            right = right + 1
        elif user != check:
            print('Incorrect...❌')
            print('The answer is', check)
    print('You have got', right, 'out of', times)
elif typ == subtraction:
    for x in range(times):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(a, '-', b, 'equals?')
        user = int(input())
        check = a - b
        if user == check:
            print('Correct ✔!')
            right = right + 1
        elif user != check:
            print('Incorrect...❌')
            print('The answer is', check)
    print('You have got', right, 'out of', times)
elif typ != addition and typ != subtraction:
    print('please choose one of the above')
