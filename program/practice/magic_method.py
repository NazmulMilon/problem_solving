class MyClass:
    def __init__(self, var):
        self.var = var

    def __del__(self):
        del self.var
