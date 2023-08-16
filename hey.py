def main():
    name = input("What's your name? ")
    print(hey(name))

def hey(to="world"):
    return f"hey, {to}"

if __name__=="__main__":
    main()