def fizzbuzz(number: int):
    for n in range(1, number+1):
        if n % 3 == 0 and n % 5 == 0:
            print(f"{n}: FizzBuzz")
        elif n % 3 == 0:
            print(f"{n}: Fizz")
        elif n % 5 == 0:
            print(f"{n}: Buzz")
        elif n == 0:
            continue
    
def main():
    fizzyNumber = int(input("Enter a number for FizzBuzz: "))
    fizzbuzz(fizzyNumber)

if __name__ == "__main__":
    main()