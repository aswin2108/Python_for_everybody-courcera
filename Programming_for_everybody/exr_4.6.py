def computepay(h, r):
    if(h>40):
        return (40*r)+((h-40)*1.5*r)
    else:
        return h*r

hrs = input("Enter Hours:")
rate=input("Enter rate:")
h=float(hrs)
r=float(rate)
p = computepay(h, r)
print("Pay", p)