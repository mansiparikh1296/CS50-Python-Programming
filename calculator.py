"""x = float(input("What's x? "))
y = float(input("What's y? "))

z= x/y
a=x+y

print(f"{z:.2f}")
print(f"{a:,}")"""

def main():
    x=int(input("What's x ? "))
    print(f"Square of x is : {square(x)}")

def square(n):
    return pow(n,2)

main()
