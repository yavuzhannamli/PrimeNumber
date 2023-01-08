number = int(input('number: '))
isprime = True

if number == 1:
    isprime = False

for i in range(2, number):
    if (number % i == 0):
        isprime = False
        break

if isprime:
    print('Number is Prime.')
else:
    print('Number is not Prime.')