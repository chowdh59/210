# Question 3A
number1 = input(" Please enter the first number: ") (1)
number2 = input(" Please enter the second number: ") (1)

# Using operator and arithmetic to add two number
sum = float(number1) + float(number2) 1
print('The sum of {0} and {1} is {2}'.format(number1, number2, sum)) (1)


Run time = 4
BigO = O(1)

# Question 3B
numbers1 = [1,5,2] 1
numbers2 = [6,1,4,3] 1
res = [0]*(len(numbers1)+len(numbers2)-1) (1)
for o1,i1 in enumerate(numbers1): (n)
    for o2,i2 in enumerate(numbers2): (n)
        res[o1+o2] += i1*i2 (n2)

Run time = 3 + 2n + n^2
BigO = O(n^2)
