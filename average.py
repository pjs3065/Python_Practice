numbers = list()
index = 10

min_number = 9999
max_number = -1

while index > 0:
    numbers.append(int(input()))
    index -= 1

sum_number = 0

for number in numbers:

    sum_number += number

    if min_number > number:
        min_number = number

    if max_number < number:
        max_number = number

sum_number = sum_number - (min_number + max_number)
print(sum_number / 8)