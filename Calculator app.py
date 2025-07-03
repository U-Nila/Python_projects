a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
def calculater():
    def add(a,b):
        return a+b
    def substract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
    def modulus(a,b):
        return a%b
    def exponential(a,b):
        return a**b
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. modulus")
    print("6. Exponential")

    choice = input("Enter choice (1-6): ")

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", substract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    elif choice == '5':
        print("Result:", modulus(a, b))
    elif choice == '6':
        print("Result:", exponential(a, b))
    else:
        print("Invalid choice")

calculater()

   