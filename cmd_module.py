
def add(x,y):
  return x + y

def subz(x,y):
  return abs(x-y)

if __name__ == "__main__":
    import sys
    print(sys.argv)
    v = sys.argv[1].lower()
    valOne = int(sys.argv[2])
    valTwo = int(sys.argv[3])
    if v == "a":
        print(add(valOne, valTwo))
    elif v == "s":
        print(subz(valOne, valTwo))
    else:
        print("The value does not match any function")
        pass
