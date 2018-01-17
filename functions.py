# def say_name(name):
#     return name

# foo = say_name("will")
# print(foo)


# def add(num1=1, num2=2):
#     return num1 + num2

# num1 = add()
# print(num1) # => 3 (no conflict btw the two num1s !)

def madlibs(name, noun="shoes", adjective="red"):
    """
    Returns "Will has black boots"
    """
    return "{0} has {1} {2}".format(name, adjective, noun)

# doesn't matter the order of the keyword arguments here:
madlib = madlibs(name="Will", adjective="black", noun="boots")
print(madlib)