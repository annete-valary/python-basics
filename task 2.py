from itertools import count

for grade in range (1,31):
    print(grade)
for number in range(1,31):
    if number % 3 == 0:
        print(number)
count_no_divisible_by_3 = 0
for number in range(1,31):
    if number % 3 == 0:
        count_no_divisible_by_3+=1
print(count_no_divisible_by_3)
