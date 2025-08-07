class Person:
    def __init__(self,name,country,dop_str):
        self.name=name
        self.country=country
        year,month,day=map(int,dop_str.split("-"))
        self.birth_year=year
        self.birth_month=month
        self.birth_day=day

    def person_age(self,current_year,current_moth,current_day):
       age=current_year-self.birth_year
       return age

    
    def display_age(self,current_year,current_moth,current_day):
        age=self.person_age(current_year,current_moth,current_day)
        return (f" my name is {self.name} and I'm from {self.country} and I have {age} years old ")
    

today_year = 2025
today_month = 8
today_day = 7

person1 = Person("Qasem Abo Alia", "Palestine", "2001-08-25")
print(person1.display_age(today_year, today_month, today_day))