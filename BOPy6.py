import math

def value_U(A, B):
    if A > B:
        return B
    elif A < B:
        return A
    else:
        return A


def value_V(A, B):
    if A > B:
        return B
    elif A < B:
        return A
    else:
        return A


def value_W(A, B):
    if A > B:
        return B
    elif A < B:
        return A
    else:
        return A


a = float(input("Enter your a: "))
b = float(input("Enter your b: "))
U = value_U(a, b)
print("Function ugiver return: " + (str(U)))
V = value_V(a * b, a + b)
print("Function vgiver return: " + (str(V)))
W = value_W(U + V * V, math.pi)
print("Function wgiver return: " + (str(W)))
