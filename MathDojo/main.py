class MathDojo:
    def __init__(self):
        self.result=0
    def add(self,num,*nums):
        self.result+=num
        for n in nums:
            self.result+=n
        return self
    
    def sustract(self,num,*nums):
        self.result-=num
        for n in nums:
            self.result-=n
        return self

md=MathDojo()

x=md.add(5).add(10,2).add(2,4,6).result
print(x)


x=md.add(2).add(2,5,1).sustract(3,2).result
print(x)

x=md.sustract(5).sustract(10,6).sustract(5,4,8).result
print(x)