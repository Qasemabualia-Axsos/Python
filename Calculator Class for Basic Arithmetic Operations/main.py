class Calculator:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def error_handle(self):
        if not isinstance(self.a,int) or not isinstance(self.b,int):
            self.result="Error:the input must be Number"
            return False
        return True
    def add(self):
        if self.error_handle():
            self.result=self.a+self.b
        return self
    def substract(self):
        if self.error_handle():
            self.result=self.a-self.b
        return self
    def multiply(self):
        if self.error_handle():
            if self.error_handle():
                self.result=self.a*self.b
        return self
    def divide (self):
        if self.b==0:
            self.result= "Error:Divesion by zero"
        else:
            self.result=self.a/self.b
        return self
    def show_result(self):
        print(f"Result:{self.result}")
        return self
    
cal=Calculator(10,5)
cal.add().show_result()
cal.substract().show_result()
cal.multiply().show_result()
cal.divide().show_result()
print("---------------")
cal=Calculator(100,0)
cal.add().show_result()
cal.substract().show_result()
cal.multiply().show_result()
cal.divide().show_result()
print("---------------")
cal=Calculator("Qasem",20)
cal.add().show_result()
cal.substract().show_result()
cal.multiply().show_result()

