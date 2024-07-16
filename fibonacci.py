def fibonaaciSequence(steps: int):
    n1 = 0
    n2 = 1
    next_number = n2
    count = 1
    while count <= steps:
        print(next_number)
        count += 1
        n1 = n2
        n2 = next_number
        next_number = n1 + n2
    print()    
    
def main():
    fibNumber = int(input("How many Fibonacci steps? "))
    fibonaaciSequence(fibNumber)

if __name__ == "__main__":
    main()