'''
Given an integer. perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''
A single line containing a positive integer, .
#!/bin/python3

def weird_checker(num):
    if num % 2 == 0:
        if 2 <= num <= 5: print("Not Weird") 
        elif 6 <= num <= 20: print("Weird")
        else: print("Not Weird")
    else: print("Weird") # print if number is ODD 1,3,5,7 ...
    
num = int(input())
weird_checker(num)
