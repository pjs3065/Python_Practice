import sys
number = []

for i in range(5):
    temp = input('Enter number between 1 and 30 : ')
    num = int(temp)
    if num < 1 or num > 30:
        print('You typed wrong range number!')
        sys.exit(-1)
    number.append(num)

star = '*'
for c in number:
    print(star * c)