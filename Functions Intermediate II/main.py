#1-Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
students[0]["last_name"]="Bryant"
sports_directory["soccer"][0]="Andres"
z[0]["y"]=30

print(x)
print(students)
print(sports_directory)
print(z)

#2-Iterate Through a List of Dictionaries
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' :'John' , 'last_name' : 'rosales'},
    {'first_name' :'Mark' , 'last_name' : 'Guillen'},
    {'first_name' :'KB' , 'last_name' : 'Tonel'}
]
def iterateDictionary(z):
    for player in z:
        print(f"first_name - {player['first_name']}, last_name - {player['last_name']}")
iterateDictionary(students)

# 3- get valuse from a list of dictionaries
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' :'John' , 'last_name' : 'rosales'},
    {'first_name' :'Mark' , 'last_name' : 'Guillen'},
    {'first_name' :'KB' , 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name,z):
    for player in z:
        print(player[key_name])


iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

# 4- iterate through a dictionary with list values
dojo = {
    'locations': ['San Jose','Seattle','Dalas','Chicago','Tulsa','DC','Burbank'],
    'instructors':['Michael','Amy','Eduardo','Josh','Graham','Patrick','Minh','Devon']
}
def printInfo(z):
    for key in z:
        print(len(z[key]),key.upper())
        for value in z[key]:
            print(value)
printInfo(dojo)