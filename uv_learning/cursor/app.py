from typing import Union, List
import math

class Calculator:
    """A calculator class with basic and advanced mathematical operations."""
    
    @staticmethod
    def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        return x + y
    
    @staticmethod
    def subtract(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        """Subtract y from x."""
        return x - y
    
    @staticmethod
    def multiply(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        return x * y
    
    @staticmethod
    def divide(x: Union[int, float], y: Union[int, float]) -> float:
        """Divide x by y."""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    
    @staticmethod
    def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Calculate base raised to the power of exponent."""
        return math.pow(base, exponent)
    
    @staticmethod
    def square_root(x: Union[int, float]) -> float:
        """Calculate the square root of a number."""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(x)
    
    @staticmethod
    def factorial(n: int) -> int:
        """Calculate the factorial of a number."""
        if not isinstance(n, int):
            raise TypeError("Factorial is only defined for integers")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return math.factorial(n)
    
    @staticmethod
    def average(numbers: List[Union[int, float]]) -> float:
        """Calculate the average of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def percentage(value: Union[int, float], total: Union[int, float]) -> float:
        """Calculate what percentage value is of total."""
        if total == 0:
            raise ValueError("Total cannot be zero")
        return (value / total) * 100

def main():
    """Main entry point for the cursor application."""
    calc = Calculator()
    
    # Example usage
    print("Calculator Demo:")
    print(f"Addition: {calc.add(5, 3)}")
    print(f"Subtraction: {calc.subtract(10, 4)}")
    print(f"Multiplication: {calc.multiply(6, 7)}")
    print(f"Division: {calc.divide(15, 3)}")
    print(f"Power: {calc.power(2, 3)}")
    print(f"Square Root: {calc.square_root(16)}")
    print(f"Factorial: {calc.factorial(5)}")
    print(f"Average: {calc.average([1, 2, 3, 4, 5])}")
    print(f"Percentage: {calc.percentage(25, 100)}%")

if __name__ == "__main__":
    main()
