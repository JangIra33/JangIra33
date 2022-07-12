def isinteger(s):
    return s.isdigit() or \
           s != '' and s[0] == '-' and s[1:].isdigit()

def isfixed(s):
    (num, dot, fraction) = s.partition('.')
    return dot == '' and fraction == '' and isinteger(num) or\
        dot == '.' and (num == '' or num == '-') and fraction.isdigit() or\
            fraction == '' and isinteger(num) or\
                isinteger(num) and fraction.isdigit()

def isfloat(s):
    (signuficand, e, exponent) = s.partition('e')
    return e == '' and exponent =='' and isfixed(signuficand) or\
        e == 'e' and isfixed(signuficand) and isinteger(exponent)

# Test code
print(isfloat("2"))       # True
print(isfloat("-2"))      # True
print(isfloat(".112"))    # True
print(isfloat("-.112"))   # True
print(isfloat("3.14"))    # True
print(isfloat("-3.14"))   # True
print(isfloat("5."))      # True
print(isfloat("5.0"))     # True
print(isfloat("-777.0"))  # True
print(isfloat("-777."))   # True
print(isfloat("."))       # False
print(isfloat(".."))      # False
print(isfloat("0e3"))     # True
print(isfloat("1.3e0"))   # True
print(isfloat("0.1e3"))   # True
print(isfloat("1e3"))     # True
print(isfloat("1.314e4")) # True
print(isfloat("-1.1e-2")) # True
print(isfloat(".3e4"))    # True
print(isfloat("2.e-2"))   # True
print(isfloat("0e3"))     # True