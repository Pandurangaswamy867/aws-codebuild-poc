# src/main.py

from calculator import add, subtract, multiply, divide

def main():
    print("Addition: ", add(5, 3))
    print("Subtraction: ", subtract(10, 4))
    print("Multiplication: ", multiply(6, 7))
    print("Division: ", divide(20, 5))

if __name__ == "__main__":
    main()
