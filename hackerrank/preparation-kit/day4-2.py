"""
Recursive Digit Sum
We define super digit of an integer  using the following rules:

if x has only 1 digit: then its super digit is x.
otherwise: the super digit of x is equal to the super digit of the sum of the digit of x
string n: a string representation of an integer
int k: the times to concatenate n to make p
n * k 를 만들고 난 뒤, 이를 만들어야 한다.
"""


def get_super_digit(digit):
    # if x has only 1 digit, then its super digit is x
    if len(digit) <= 1:
        return digit

    s = 0
    for c in digit:
        s += int(c)

    return get_super_digit(str(s))


def superDigit(n, k):
    # Write your code here
    s = int(get_super_digit(n)) * k
    return get_super_digit(str(s))


n = "9875"
k = 4
print(superDigit(n, k))
