class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Jar most not be leff than zero!!")
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return f"🍪 * {self.cookies}"

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
        return self.capacity

    @property
    def size(self):
        return self.cookies
