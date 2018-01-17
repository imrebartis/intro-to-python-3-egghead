def total(n):
    tax_rate = .07
    return n * tax_rate + n

def tax_amount(n):
    tax_rate = .07
    return n * tax_rate

# making it possible to use the total function directly in the terminal
# e.g. python3 tax.py 10
if __name__ == "__main__":
    import sys
    print(total(int(sys.argv[1])))