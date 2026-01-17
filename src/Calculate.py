class Calculate: 
    def __init__(self, num = 0): 
        self.num = num; 
    
    def increase(self, num):
        self.num = self.num + num; 
    
    def display(self): 
        print(self.num)

calculate = Calculate(1)
calculate.increase(5)

calculate.display()
