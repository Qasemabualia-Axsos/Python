#1-Basic - Print all integers from 0 to 150.
for x in range (0,151):
    print (x)

#2-Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range (5,1001,5):
    print (x)

#3-Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible
for num in range (1,101):
    if num%10==0:
        print ("Coding Dojo")
    elif num%5==0:
        print ("Coding")
    else:
        print(num)

#4-Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for num in range(1,500001,2):
    sum+=num
print (sum) 

#5-Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for num in range (2018,0,-4):
    print (num)

#6-Flexible Counter
lowNum=2
highNum=9
mult=3
for i in range(lowNum,highNum+1):
    if i % mult ==0:
        print(i)
