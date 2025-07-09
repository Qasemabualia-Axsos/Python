# 1. TASK: print "Hello World"
print( "Hello World" )

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( "Hello",name,"!")
print( "Hello"+" "+name +"!" )

# 3. print "Hello 42!" with the number in a variable
name = 42
print( "Hello", name ,"!")
# print( "Hello" +name+"!")----->Error
print("Hello"+" "+ str(name)+"!")

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print ("I love to eat {} and {}.".format(fave_food1,fave_food2))
print(f"I love to eat {fave_food1} and {fave_food2}.")