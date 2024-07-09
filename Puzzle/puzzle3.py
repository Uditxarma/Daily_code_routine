"""Write a Python program that accepts an integer and determines 
    whether it is greater than 4^4 and which is 4 mod 34. """

num =914
if num>4*4:
    print("num is greater than 4*4")
    if num%34 ==4:
        print("True")
    else:
        print("False")