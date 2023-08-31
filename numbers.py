# def average(a=9,b=1):
#     print("the average of a and b is:", (a+b)/2)
# average(b=8)
# average(b=11,a=7)

def average(*numbers):
    print(type(numbers))
    sum = 0 #this line specifies that the sum is intially zero
    for i in numbers:
        sum += i
    print("average is:", sum/len(numbers))
average(5,6,10)





    