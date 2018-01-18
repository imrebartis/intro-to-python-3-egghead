def whoami():
    def local_groot():
        i = "I am local groot"
        print(id(i)) # => 4356426896
        print(i)

    def nonlocal_groot():
        nonlocal i
        i = "I am nonlocal groot"

    def global_groot(name):
        return "I am {0} groot".format(name)

    i = "I am groot"
    print(id(i)) # => 4356455792
    print(i) # => I am groot
    local_groot() # => I am local groot
    print(id(i)) # => 4356455792
    print(i) # => I am groot
    nonlocal_groot()
    print(i) # => I am nonlocal groot
    print(global_groot("the only")) # => I am the only groot
    print(i) # => I am nonlocal groot

whoami()