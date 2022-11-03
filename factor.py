c = input("Enter factor A: ")
d = input("Enter factor B: ")
#fctrs = (a, b)
def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False

print(is_factor(c, d))