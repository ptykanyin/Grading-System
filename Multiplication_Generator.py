print("Multiplication Generator")
name = input("Hello, What is your name?")
print("Hii" + name)
multiplicator =int(input("Please input your multiplicator ="))
bound = int(input("Input your bound ="))


def multiplicationtable(multiplicator, bound):
    for i in range(1,bound+1):
        print(f"{multiplicator} x {i} = {multiplicator*i}")



multiplicationtable(multiplicator,bound)


