class decorator():
    def __init__(self,capital):
        self.capital=capital

    def __call__(self):
        str1=self.capital()
        return str1.upper()
@decorator
def wish():
    return "happy birthday"
print(wish())
    