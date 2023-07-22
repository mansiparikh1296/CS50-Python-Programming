def hello(n="world"):
    print("Hello,",n)

def main():
    hello()
    #Ask user their name 
    name = input("What's your name? ")
    hello(name)

main()

