class MyClass:
    def __init__(self, var):
        self.var = var

    def __del__(self):
        del self.var

    def __gt__(self, other):
        return len(other)>len(self.var)

    def __lt__(self, other):
        return len(other)<len(self.var)

    def __ge__(self, other):
        return len(other)>=len(self.var)

    def __le__(self, other):
        return len(other)<=len(self.var)
    