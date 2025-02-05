class Jar:
    def __init__(self, capacity=12):
        #if capacity :
        #    raise ValueError("Invalid name")
        self.ccapacity = capacity
        self.cookies = 0

    def __str__(self):
        🍪

    def deposit(self, n):
        if self.cookies + n > self.ccapacity:
            raise ValueError("Jar is full!")
        else:
            self.cookies += n

    def withdraw(self, n):
        if self.cookies - n < 0:
            raise ValueError("No more Cookies left!")
        else:
            self.cookies -= n

    @property
    def capacity(self):
        return self.ccapacity

    @property
    def size(self):
        return self.cookies
