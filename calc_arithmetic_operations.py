def arithmetic_operations(first, second):
    addition = first + second
    subtraction = first - second
    multiplication = first * second
    division = first / second
    division_truncate = first // second
    remainder = first % second
    exponentiation = first ** second

    print(f"Addition = {addition}")
    print(f"Subtraction = {subtraction}")
    print(f"Multiplication = {multiplication}")
    print(f"Division = {division}")
    print(f"Division truncate = {division_truncate}")
    print(f"Remainder = {remainder}")
    print(f"Exponentiation = {exponentiation}")


if __name__ == "__main__":
    first = int(input("Enter the first integer number: "))
    second = int(input("Enter the second integer number: "))
    arithmetic_operations(first, second)