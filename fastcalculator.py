print("Welcome to my FASTCalculator")

what = input ("Why action? (+,-,/,): ")

a = float(input("Write  One number: "))
b = float(input("Write two number: "))

if what == "+":
    e = a + b
    print ("Result " + str(c))
elif what == "-":
    e = a - b
    print ("Result: " + str(c))
elif what == "":
    e = a * b 
    print ("Result: " + str(c))
elif what == "/":
    e = a / b
    print ("Result: " + str(c))
else:
    print ("Error)

input ()
