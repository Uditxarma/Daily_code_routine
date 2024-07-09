'''Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least 
    three occurrences of five. Return True otherwise False. '''

l= [19, 19, 15, 5, 3, 5, 5, 2]
if l.count(19)==2 and l.count(5)==3:
    print("True")
else:
    print("False")