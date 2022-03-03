import math as m
e=2,7182
a=2.5
b=0.5
x=8
f = m.sqrt(a*x*x+b*x)-m.exp((-a*x))
y = m.log(x)*(x*m.atan(a*x)-m.sqrt(abs(x**3))+m.log(abs(b*x))+3)
print("При x=8: ",y,f)
x=1
y = m.log(x)*(x*m.atan(a*x)-m.sqrt(abs(x**3))+m.log(abs(b*x))+3)
print("При x=1: ",y,f)