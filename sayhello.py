import cowsay 
import pyttsx3

def sayHello(greeting: str):
    engine = pyttsx3.init()
    cowsay.tux(greeting)
    engine.say(greeting)
    engine.runAndWait()

def main():
    greeting = input("What do you want to say? ")
    sayHello(greeting)

if __name__ == "__main__":
    main()