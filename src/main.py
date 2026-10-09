
from utils import square, is_even, celsius_to_fahrenheit


def main():
    number = float(input("Enter a number: "))

    print(f"Square: {square(number):g}")
    print(f"Even: {'Yes' if is_even(number) else 'No'}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(number):g}")


if __name__ == "__main__":
    main()
