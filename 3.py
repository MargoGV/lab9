s=int(input())
y=int(input())
x=float(input())/100
z=((s*(1+x)**y)*((1+x)**(1/12)-1))/((1+x)**y-1)
print(z)
print((z*y*12)-s)
