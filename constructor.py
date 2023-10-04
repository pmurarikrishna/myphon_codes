class CheckPositiveNumber:
    def __init__(self, number):
        self.number = number

    def __call__(self):
        if self.number > 0:
            print("Number is positive")
        else:
            print("Number is negative")    

ans=CheckPositiveNumber(-5)
ans()