
def climbStairs(n):
    if n <= 1:
        return 1
    twoSteps = 1
    oneStep = 1
    for i in range(2, n+1):
        current = twoSteps + oneStep
        twoSteps = oneStep
        oneStep = current
    
    return oneStep

def main():
    steps = int(input("How many stairs do you want to climb? "))
    print(climbStairs(steps))
    
if __name__ == "__main__":
    main()