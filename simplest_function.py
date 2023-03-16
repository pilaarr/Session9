def my_simplest_function():
    pass  # do nothing, used for things to do (leave it blank and come back later)



def greet():
    print("Hello dear, hope you're doing fine")


for i in range(10):  # to print it 10 times
    print(f"{i+1} ", end="")
    greet()

x = greet()
print(x)  # returns none because it has no output (print does not return any value)
y = print("Hello world")
print(y)  # also returns none