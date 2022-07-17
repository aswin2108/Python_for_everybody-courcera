hrs = input("Enter Hours:")
rate=input("Enter rate:")
h = float(hrs)
r=float(rate)
pay=0
extra=1
if h>40:
    pay=(40*r)+((h-40)*r*1.5)
else:
    pay=h*r
print(pay)