'''
The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
Note that "" represents the consecutive values in between.

Example
n = 5
Print the string 12345
'''

num = int(input())

for num in range(1,num+1): # num + 1 allow us to print the given user number also. As range function second's parameter prints from 1 to n - 1 by default
    print(num,end='') # end with empty quote allow us to print value without newline as by default each element traverse via Loop print in newline
    
