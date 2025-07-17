#1-Biggie Size
def biggie_size(list):
    for i in range (len(list)):
        if list[i]>0:
            list[i]="big"
    return list
print (biggie_size([-1, 3, 5, -5]))

#2-Count Positives
def count_positives(list):
    sum=0
    for i in range (len(list)):
        if list[i]>0:
            sum+=1
    list[-1]=sum        
    return list
print (count_positives([-1,1,1,1])) 
print (count_positives([1,6,-4,-2,-7,-2])) 

#3=Sum Total
def length(list):
    sum=0
    for i in range (len(list)):
        sum+=list[i]
    return sum
print (length([1,2,3,4]))
print (length([6,3,-2]))

#4-Average
def avarage(list):
    sum=0
    for i in range (len(list)):
        sum+=list[i]
    avg=sum/len(list)
    return avg
print (avarage([1,2,3,4]))

#5-Length
def length(list):
    counter=0
    for i in range (len(list)):
        counter+=1
    return counter
print (length([37,2,1,-9]))
print (length([]))

#6-Minimum
def minimum(list):
    if len(list)==0:
        return False
    result=list[0]
    for i in range (len(list)):
        if list[i]<result:
            result=list[i]
    return result
print (minimum([37,2,1,-9]))
print (minimum([]))

#7-Maximum
def maximum(list):
    if len(list)==0:
            return False
    result=list[0]
    for i in range (len(list)):
        if list[i]>result:
            result=list[i]
    return result
print (maximum([37,2,1,-9]))
print (maximum([]))

#8-Ultimate Analysis
def ultimate_analysis(list):
    if len(list)==0:
        return False
    sum=0
    min=list[0]
    max=list[0]
    for i in range (len(list)):
        sum+=list[i]
        if list[i]<min:
            min=list[i]
        if list[i]>max:
            max=list[i]
    Avg=sum/len(list)
    result={
        'sumTotal': sum,
        'average':Avg,
        'minimum':min,
        'maximum':max,
        'length':len(list)
    }
    return result
print (ultimate_analysis([37,2,1,-9]))
    
#9-Reverse List
def reverse_list(list):
    for i in range (len(list)//2):
       list[i],list[-1-i]=list[-1-i],list[i]
    return list
print (reverse_list([37,2,1,-9]))


