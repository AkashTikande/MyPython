
import math

class EngineeringCalculator:
    def __init__(self):
        self.memory = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def power(self, x, y):
        return x ** y   # power 2 ** 3 = 8

    def square_root(self, x):
        return math.sqrt(x)

    def sine(self, x):

        return math.sin(x)

    def cosine(self, x):
        return math.cos(x)

    def tangent(self, x):
        return math.tan(x)

    def logarithm(self, x):
        return math.log(x)

    def memory_store(self, x):
        self.memory = x

    def memory_recall(self):
        return self.memory

def main():
    calculator = EngineeringCalculator()

    while True:
        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Logarithm")
        print("11. Memory store")
        print("12. Memory recall")
        print("13. Exit")

        choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13): ")

        if choice == '13':
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = calculator.add(num1, num2)
            print(num1, "+", num2, "=", result)

        elif choice == '2':
            result = calculator.subtract(num1, num2)
            print(num1, "-", num2, "=", result)

        elif choice == '3':
            result = calculator.multiply(num1, num2)
            print(num1, "*", num2, "=", result)

        elif choice == '4':
            result = calculator.divide(num1, num2)
            print(num1, "/", num2, "=", result)

        elif choice == '5':
            result = calculator.power(num1, num2)
            print(num1, "^", num2, "=", result)

        elif choice == '6':
            result = calculator.square_root(num1)
            print("Square root of", num1, "=", result)

        elif choice == '7':
            result = calculator.sine(num1)
            print("Sine of", num1, "=", result)

        elif choice == '8':
            result = calculator.cosine(num1)
            print("Cosine of", num1, "=", result)

        elif choice == '9':
            result = calculator.tangent(num1)
            print("Tangent of", num1, "=", result)

        elif choice == '10':
            result = calculator.logarithm(num1)
            print("Logarithm of", num1, "=", result)

        elif choice == '11':
            calculator.memory_store(num1)
            print("Memory store:", num1)

        elif choice == '12':
            result = calculator.memory_recall()
            print("Memory recall:", result)

        else:
            print("Invalid input")

if __name__ == "__main__":
    main()