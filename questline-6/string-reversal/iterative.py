
t=input()
def reverse_iterative(a):
    result = ""
    for i in range(len(a)-1, -1, -1):
        result += a[i]
    return result
print(reverse_iterative(t))
