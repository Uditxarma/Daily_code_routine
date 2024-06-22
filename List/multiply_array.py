'''Write a Python program to multiply all the items in a list.'''
def multiply_list(num):
    for i in num:
        total = 1
        total= total*i
    return total

print(multiply_list([12,34,66]))