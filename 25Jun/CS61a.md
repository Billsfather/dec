print(1)
return None but have a side effect : display 1 

_Jun16_
local test:
> python3 ok -u --local 

_Jun17_

/ : truediv
// : floordiv
mod :remainder of dividing
`def divide_exact(n,d):return n // d ,n % d`
`quotinent,remainder = divide_exact(2013,10)`
 
{ ` def a_plus_abs_b(a,b):`
`    """Return a+abs(b), but without calling abs.`
`print(a_plus_abs_b(-11,-5))`
`    >>> a_plus_abs_b(2, 3)`
`    5`
`    >>> a_plus_abs_b(2, -3)`
`    5`
`    >>> a_plus_abs_b(-1, 4)`
`    3`
`    >>> a_plus_abs_b(-1, -4)`
`    3"""`
`    if b < 0:`
`       f = sub(a,b)`
`    else:`
`       f = add(a,b)`
`    return f` }

* ` python3 -m doctest -v hw01.py`: excute the doc code in a python file

* `python3 -i ex.py` : 

_Jun21_

n = 15
`for i in range(n//2,0,-1):`
   `    print(i)`
   terminal:
>>> largest_factor(15)
7
6
5
4
3
2
1

 def  hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length. ``

    >> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    step = 1
    while x != 1:
        print(x)
        if x % 2 == 0:
            x //= 2
        else:
            x = 3*x + 1
        step += 1
    print(1)
    return step 

    _Jun24_
```python
assert 2>3,'that is false'
def aera(r,shape_constant):
    assert r>0,'A length must be positive'
    return r*r*shape_constant
print('hello')
```
    
    from math import pi 
    def area_square(r):
        return area(r,1)
    def area_circle(r):
        return area(r,pi)
    def area_hexagon(r):
        return area(r,3*sqrt(3)/2)

```python
def cube(k):
    return pow(k,3)
def summation(n,term):
    """Sum the first n terms of the sequence.
    >>> summation(5,cube)
    255
    """
    total,k=0,1
    while k<=n:
        total,k=total+term(k),k+1
    return total

def cubsum(k)
    return summation(k,cube)
```
    