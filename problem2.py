#!python3
"""
##### Problem 2
Create a function that determines if a triangle is acute, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

def triangle(a,b,c):
    H = max(a,b,c)
    A = min(a,b,c)
    B = (a+b+c)-(A+H)
    if A+B < H:
        return 0
    else:
        if H**2 == (A**2 + B**2):
            return 2
        elif H**2 < A**2 + B**2:
            return 1
        elif A**2 + B**2 < H**2:
            return 3
        else:
            return 0

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()