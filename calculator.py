class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for _ in range(abs(b)):
            result = self.add(result, a)
        return result if b >= 0 else -result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = 0
        temp = abs(a)
        while temp >= abs(b):
            temp = self.subtract(temp, abs(b))
            result = self.add(result, 1)
        return result if (a > 0) == (b > 0) else -result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero")
        temp = abs(a)
        while temp >= abs(b):
            temp = self.subtract(temp, abs(b))
        return temp if a >= 0 else -temp
