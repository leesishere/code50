class Jar:
    def __init__(self, capacity=12):
        #if capacity :
        #    raise ValueError("Invalid name")
        self.ccapacity = capacity
        self.cookies = 0

    def __str__(self):
        🍪

    def deposit(self, n):
        try:
            if type(n) != int:
                raise ValueError("Invalid name")
        self.cookies += n

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
