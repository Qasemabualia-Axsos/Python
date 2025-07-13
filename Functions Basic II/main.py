#1-Countdown
def countdown(num):
    result=[]
    while num>=0:
        result.append(num)
        num-=1
    return result
print (countdown(5))

#2-Print and Return
def print_and_return(num):
    print (num[0])
    return(num[1])
result=print_and_return([1,2])
print (result)
    
#3-First Plus Length
def first_plus_length(list):
    return list[0]+len(list)
print (first_plus_length([1,2,3,4,5]))

#4-Values Greater than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    second=list[1]
    result=[]
    for i in range (len(list)):
        if list[i] > second:
            result.append(list[i])
    print(len(result))
    return result
print (values_greater_than_second([5,2,3,2,1,4]))
print (values_greater_than_second([3]))

#5-This Length, That Value
def length_and_value (size, value):
    return [value] *size
print (length_and_value(4,7))
print (length_and_value(6,2))

