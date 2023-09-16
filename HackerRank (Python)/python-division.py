'''
Reads two integers from STDIN.
Add logic to print two lines. The first line should contain the result of integer division & the The second line should contain the result of float division.
No rounding or formatting is necessary.

'''

num1 = int(input())
num2 = int(input())

print(int(num1 / num2),float(num1 / num2),sep='\n')
